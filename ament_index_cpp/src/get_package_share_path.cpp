// Copyright 2026 Open Source Robotics Foundation, Inc.
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

#include "ament_index_cpp/get_package_share_path.hpp"

#include <filesystem>
#include <string>

#include "ament_index_cpp/get_package_prefix.hpp"

namespace ament_index_cpp
{

std::filesystem::path get_package_share_path(
  const std::string & package_name)
{
  std::filesystem::path result;
  get_package_prefix(package_name, result);
  return result / "share" / package_name;
}

}  // namespace ament_index_cpp
