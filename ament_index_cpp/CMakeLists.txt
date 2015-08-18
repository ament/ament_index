cmake_minimum_required(VERSION 2.8.3)

project(ament_index_cpp)

if(NOT WIN32)
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -Wall -Wextra")
endif()

find_package(ament_cmake REQUIRED)

add_library(${PROJECT_NAME}
  src/get_resource.cpp
  src/get_resources.cpp
  src/get_search_paths.cpp)
target_include_directories(${PROJECT_NAME} PUBLIC include)

ament_export_include_directories(include)
ament_export_libraries(${PROJECT_NAME})

if(AMENT_ENABLE_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # prevent cppcheck from being found, since it fails to process the file utest.cpp
  set(ament_cmake_cppcheck_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()

  ament_add_gtest(${PROJECT_NAME}_utest test/utest.cpp)
  if(TARGET ${PROJECT_NAME}_utest)
    target_include_directories(${PROJECT_NAME}_utest
      PUBLIC "../include")
    target_link_libraries(${PROJECT_NAME}_utest ${PROJECT_NAME})
  endif()
endif()

ament_package()

install(DIRECTORY include/
  DESTINATION include)

install(TARGETS ${PROJECT_NAME}
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
  RUNTIME DESTINATION bin)
