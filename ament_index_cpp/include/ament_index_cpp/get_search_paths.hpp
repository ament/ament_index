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

#ifndef __ament_index_cpp__get_search_paths__h__
#define __ament_index_cpp__get_search_paths__h__

#include <list>
#include <string>

#include <ament_index_cpp/visibility_control.h>

namespace ament_index_cpp
{

AMENT_INDEX_CPP_PUBLIC
std::list<std::string>
get_search_paths();

}  // namespace

#endif  // __ament_index_cpp__get_search_paths__h__
