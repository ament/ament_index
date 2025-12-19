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

#include "ament_index_cpp/has_resource.hpp"

#include <fstream>
#include <stdexcept>
#include <string>

#include "ament_index_cpp/get_search_paths.hpp"

namespace ament_index_cpp
{

bool
has_resource(
  const std::string & resource_type,
  const std::string & resource_name,
  std::string * prefix_path)
{
  if (resource_type.empty()) {
    throw std::runtime_error("ament_index_cpp::has_resource() resource type must not be empty");
  }
  if (resource_name.empty()) {
    throw std::runtime_error("ament_index_cpp::has_resource() resource name must not be empty");
  }
  std::optional<std::filesystem::path> result = is_resource_available(resource_type, resource_name);
  if (result.has_value()) {
    if (prefix_path) {
      *prefix_path = result.value().string();
    }
    return true;
  }
  return false;
}

std::optional<std::filesystem::path>
is_resource_available(
  const std::string & resource_type,
  const std::string & resource_name)
{
  std::optional<std::filesystem::path> result = std::nullopt;

  auto paths = get_searcheable_paths();
  for (auto path : paths) {
    auto resource_path = path / "share" / "ament_index" / "resource_index" /
      resource_type / resource_name;
    std::ifstream s(resource_path.string());
    if (s.is_open()) {
      result = path;
      return result;
    }
  }
  return result;
}

}  // namespace ament_index_cpp
