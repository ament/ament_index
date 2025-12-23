// Copyright 2015 Open Source Robotics Foundation, Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#include "ament_index_cpp/get_resources.hpp"

#include <filesystem>
#include <map>
#include <string>

#include "ament_index_cpp/get_search_paths.hpp"

namespace ament_index_cpp
{

std::map<std::string, std::filesystem::path>
get_resources_by_name(const std::string & resource_type)
{
  if (resource_type.empty()) {
    throw std::runtime_error("ament_index_cpp::get_resources() resource type must not be empty");
  }
  std::map<std::string, std::filesystem::path> resources;
  auto paths = get_searcheable_paths();
  for (auto base_path : paths) {
    auto path = base_path / "share" / "ament_index" / "resource_index" / resource_type;

    if (!std::filesystem::exists(path)) {
      continue;
    }

    for (auto const & dir_entry : std::filesystem::directory_iterator{path}) {
      if (std::filesystem::is_directory(dir_entry.path())) {
        continue;
      }

      auto filename = dir_entry.path().filename();

      // ignore files starting with a dot
      if (filename.c_str()[0] == '.') {
        continue;
      }

      if (resources.find(filename.string()) == resources.end()) {
        resources[filename.string()] = base_path;
      }
    }
  }
  return resources;
}

std::map<std::string, std::string>
get_resources(const std::string & resource_type)
{
  std::map<std::string, std::string> result;
  std::map<std::string, std::filesystem::path> resources = get_resources_by_name(resource_type);
  for (const auto & resource : resources) {
    result[resource.first] = resource.second.string();
  }
  return result;
}

}  // namespace ament_index_cpp
