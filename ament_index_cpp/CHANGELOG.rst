^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package ament_index_cpp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Forthcoming
-----------

1.0.6 (2021-05-06)
------------------

1.0.5 (2021-04-14)
------------------
* Remove Claire as the maintainer. (`#71 <https://github.com/ament/ament_index/issues/71>`_)
* Contributors: Chris Lalancette

1.0.4 (2021-04-06)
------------------
* Change links from index.ros.org -> docs.ros.org (`#70 <https://github.com/ament/ament_index/issues/70>`_)
* Contributors: Chris Lalancette

1.0.3 (2021-03-18)
------------------
* Add Audrow as a maintainer (`#68 <https://github.com/ament/ament_index/issues/68>`_)
* Contributors: Audrow Nash

1.0.2 (2021-01-25)
------------------
* update maintainers (`#67 <https://github.com/ament/ament_index/issues/67>`_)
* Contributors: Claire Wang

1.0.1 (2020-10-07)
------------------
* Update QD to Quality Level 1 (`#66 <https://github.com/ament/ament_index/issues/66>`_)
* add rational why ament_index pkgs don't have explicit performance tests (`#65 <https://github.com/ament/ament_index/issues/65>`_)
* Fixed Doxygen warnings (`#63 <https://github.com/ament/ament_index/issues/63>`_)
* Remove the Quality Level from the README.md. (`#62 <https://github.com/ament/ament_index/issues/62>`_)
* Update QD ament_index_cpp to QL 2 (`#59 <https://github.com/ament/ament_index/issues/59>`_)
* Add Security Vulnerability Policy pointing to REP-2006. (`#57 <https://github.com/ament/ament_index/issues/57>`_)
* [Quality Declaration] Update Version Stability to stable version (`#58 <https://github.com/ament/ament_index/issues/58>`_)
* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Dirk Thomas, brawner

1.0.0 (2020-05-22)
------------------
* Add entry page for API documentation (`#56 <https://github.com/ament/ament_index/issues/56>`_)
* Added Doxygen and Sphinx (`#55 <https://github.com/ament/ament_index/issues/55>`_)
* Add Quality Declaration level 4 ament_index_cpp (`#53 <https://github.com/ament/ament_index/issues/53>`_)
* Added docblock to ament_index_cpp (`#52 <https://github.com/ament/ament_index/issues/52>`_)
* Contributors: Alejandro Hernández Cordero, Jorge Perez

0.8.0 (2020-04-17)
------------------
* use ament_export_targets() (`#51 <https://github.com/ament/ament_index/issues/51>`_)
* Revert 46 (`#48 <https://github.com/ament/ament_index/issues/48>`_)
* Address clang-tidy warnings (`#47 <https://github.com/ament/ament_index/issues/47>`_)
* Refactor paths to use rcpputils filesystem helper (`#46 <https://github.com/ament/ament_index/issues/46>`_)
* Increase test coverage ament_index_cpp (`#40 <https://github.com/ament/ament_index/issues/40>`_)
* Contributors: Anas Abou Allaban, Chris Lalancette, Dirk Thomas, Jorge Perez

0.7.2 (2019-10-16)
------------------
* 0.7.2
* Contributors: Dirk Thomas

0.7.1 (2019-09-18)
------------------

0.7.0 (2019-04-11)
------------------
* enable cppcheck (`#32 <https://github.com/ament/ament_index/issues/32>`_)
* Contributors: Dirk Thomas

0.5.1 (2018-06-18 13:50)
------------------------

0.5.0 (2018-06-18 13:25)
------------------------
* pass HAS_LIBRARY_TARGET to ament_export_interfaces (`#30 <https://github.com/ament/ament_index/issues/30>`_)
* honor BUILD_SHARED_LIBS (`#28 <https://github.com/ament/ament_index/issues/28>`_)
* Contributors: Dirk Thomas, Mikael Arguedas

0.4.0 (2017-12-08)
------------------
* add package resource related utility functions to cpp API (`#27 <https://github.com/ament/ament_index/issues/27>`_)
* 0.0.3
* 0.0.2
* use CMAKE_X_STANDARD and check compiler rather than platform
* use ament_cmake_export_interfaces
* add pedantic flag
* c++14 (`#21 <https://github.com/ament/ament_index/issues/21>`_)
* More ament resource index cpp tests (`#18 <https://github.com/ament/ament_index/issues/18>`_)
* expose prefix path from get_resource, add C++ has_resource
* update schema url
* add schema to manifest files
* require CMake 3.5
* use CTest BUILD_TESTING
* fix sign compare warning with newer compiler
* Ignore subdirectories and dotfiles in get_resources
* Added missing include
* update unit tests to match `#10 <https://github.com/ament/ament_index/issues/10>`_
* fix finding resources in overlayed workspaces
* update style to pass ament_cpplint
* fix directory check on Windows
* add visibility macros
* fix include dir of test
* fix syntax error in Windows code
* make library shared
* add ament_index_cpp package
* Contributors: Deanna Hood, Dirk Thomas, Esteve Fernandez, Mikael Arguedas, William Woodall, dhood
