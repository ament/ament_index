# Copyright 2015-2019 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from pathlib import Path
from typing import Literal

from .constants import RESOURCE_INDEX_SUBFOLDER
from .search_paths import get_search_paths


class InvalidResourceTypeNameError(ValueError):
    """Raised when a resource type name is invalid."""


class InvalidResourceNameError(ValueError):
    """Raised when a resource name is invalid."""


def _name_is_invalid(resource_name: str) -> bool:
    """
    Get the whether a resource name or a resource type name is invalid.

    This is not considered public API.

    A name is considered invalid if it contains any path separators. The index represents resources
    as files and resource types as folders so allowing path separators causes issues.

    For a more complete discussion, see: https://github.com/ament/ament_index/pull/69

    :param resource_name: the name of the resource or resource type
    :type resource_name: str
    :returns: True or False
    """
    return ('/' in resource_name) or ('\\' in resource_name)


def get_resource(resource_type: str, resource_name: str) -> tuple[str, str]:
    """
    Get the content of a specific resource and its prefix path.

    :param resource_type: the type of the resource
    :type resource_type: str
    :param resource_name: the name of the resource
    :type resource_name: str
    :returns: a tuple of the content (bytes) of the resource and its prefix path
    :raises: :exc:`OSError`
    :raises: :exc:`LookupError`
    :raises: :exc:`InvalidResourceTypeNameError`
    :raises: :exc:`InvalidResourceNameError`
    """
    if not resource_type:
        raise ValueError('The resource type must not be empty')
    if not resource_name:
        raise ValueError('The resource name must not be empty')
    if _name_is_invalid(resource_type):
        raise InvalidResourceTypeNameError(
            f"Resource type '{resource_type}' is invalid")
    if _name_is_invalid(resource_name):
        raise InvalidResourceNameError(
            f"Resource name '{resource_name}' is invalid")
    for path in get_search_paths():
        resource_path = Path(path, RESOURCE_INDEX_SUBFOLDER, resource_type, resource_name)
        if resource_path.is_file():
            try:
                content = resource_path.read_text(encoding='utf-8')
            except OSError as e:
                raise OSError(
                    f"Could not open the resource '{resource_name}' of type "
                    f"'{resource_type}':\n{e}") from e
            return content, path
    raise LookupError(
        f"Could not find the resource '{resource_name}' of type '{resource_type}'")


def get_resources(resource_type: str) -> dict[str, str]:
    """
    Get the resource names of all resources of the specified type.

    :param resource_type: the type of the resource
    :type resource_type: str
    :returns: dict of resource names to the prefix path they are in
    :raises: :exc:`OSError`
    :raises: :exc:`InvalidResourceTypeNameError`
    """
    if not resource_type:
        raise ValueError('The resource type must not be empty')
    if _name_is_invalid(resource_type):
        raise InvalidResourceTypeNameError(
            f"Resource type '{resource_type}' is invalid")
    resources = {}
    for path in get_search_paths():
        resource_path = Path(path, RESOURCE_INDEX_SUBFOLDER, resource_type)
        if resource_path.is_dir():
            with os.scandir(resource_path) as entries:
                for entry in entries:
                    # Ignore subdirectories, and anything starting with a dot
                    if entry.is_dir() or entry.name.startswith('.'):
                        continue
                    if entry.name not in resources:
                        resources[entry.name] = path
    return resources


def get_resource_types() -> set[str]:
    """
    Get the resource types.

    :returns: set of resource types within the search paths
    :raises: :exc:`OSError`
    """
    resource_types = set()
    for path in get_search_paths():
        basepath = Path(path, RESOURCE_INDEX_SUBFOLDER)
        if basepath.is_dir():
            with os.scandir(basepath) as entries:
                for entry in entries:
                    # Ignore non-subdirectories, and anything starting with a dot
                    if not entry.is_dir() or entry.name.startswith('.'):
                        continue
                    resource_types.add(entry.name)
    return resource_types


def has_resource(resource_type: str, resource_name: str) -> str | Literal[False]:
    """
    Check if a specific resource exists.

    :param resource_type: the type of the resource
    :type resource_type: str
    :param resource_names: the name of the resource
    :type resource_name: str
    :returns: The prefix path if the resource exists, False otherwise
    :raises: :exc:`OSError`
    :raises: :exc:`InvalidResourceTypeNameError`
    :raises: :exc:`InvalidResourceNameError`
    """
    assert resource_type, 'The resource type must not be empty'
    assert resource_name, 'The resource name must not be empty'
    if _name_is_invalid(resource_type):
        raise InvalidResourceTypeNameError(
            f"Resource type '{resource_type}' is invalid")
    if _name_is_invalid(resource_name):
        raise InvalidResourceNameError(
            f"Resource name '{resource_name}' is invalid")
    for path in get_search_paths():
        resource_path = Path(path, RESOURCE_INDEX_SUBFOLDER, resource_type, resource_name)
        if resource_path.is_file():
            return path
    return False
