
This document is a declaration of software quality for the `ament_index_python` package, based on the guidelines in [REP-2004](https://www.ros.org/reps/rep-2004.html).

# `ament_index_python` Quality Declaration

The package `ament_index_python` claims to be in the **Quality Level 1** category.

Below are the rationales, notes, and caveats for this claim, organized by each requirement listed in the [Package Requirements for Quality Level 1 in REP-2004](https://www.ros.org/reps/rep-2004.html).

## Version Policy

### Version Scheme

`ament_index_python` uses `semver` according to the recommendation for ROS Core packages in the [ROS 2 Developer Guide](https://index.ros.org/doc/ros2/Contributing/Developer-Guide/#versioning), and is at or above a stable version, i.e. `>= 1.0.0`.

### API Stability Within a Released ROS Distribution

`ament_index_python` will not break public API within a released ROS distribution, i.e. no major releases once the ROS distribution is released.

### ABI Stability Within a Released ROS Distribution

`ament_index_python` contains python code, TODO: define policy to handle ABI for python packages of the ROS Core.

### Public API Declaration

TODO: Define API for this package

## Change Control Process

`ament_index_python` follows the recommended guidelines for ROS Core packages in the [ROS 2 Developer Guide](https://index.ros.org/doc/ros2/Contributing/Developer-Guide/#change-control-process).

This includes:

- all changes occur through a pull request
- all pull request have two peer reviews
- all pull request must pass CI on all [tier 1 platforms](https://www.ros.org/reps/rep-2000.html#support-tiers)
- all pull request must resolve related documentation changes before merging

## Documentation

### Feature Documentation

TODO fix link

`ament_index_python` has a [feature list](TODO) and each item in the list links to the corresponding feature documentation.
There is documentation for all of the features, and new features require documentation before being added.

### Public API Documentation

TODO fix link

`ament_index_python` has embedded API documentation and it is generated using doxygen and is [hosted](TODO) along side the feature documentation.
There is documentation for all of the public API, and new additions to the public API require documentation before being added.

### License

The license for `ament_index_python` is Apache 2.0, and a summary is in each source file, the type is declared in the `package.xml` manifest file, and a full copy of the license is in the `LICENSE` file.

There is an automated test which runs a linter (ament_copyright) that ensures each file has a license statement.

### Copyright Statements

The copyright holders each provide a statement of copyright in each source code file in `ament_index_python`.

There is an automated test which runs a linter (ament_copyright) that ensures each file has at least one copyright statement.

## Testing

### Feature Testing

Each feature in `ament_index_python` has corresponding tests which simulate typical usage, and they are located in the `test` directory.
New features are required to have tests before being added.

### Public API Testing
TODO: Define API for this package

Each part of the public API have tests, and new additions or changes to the public API require tests before being added.
The tests aim to cover both typical usage and corner cases, but are quantified by contributing to code coverage.

### Coverage

TODO fix link

`ament_index_python` follows the recommendations for ROS Core packages in the [ROS 2 Developer Guide](https://index.ros.org/doc/ros2/Contributing/Developer-Guide/#coverage), and opts to use branch coverage instead of line coverage.

This includes:

- tracking and reporting branch coverage statistics
- achieving and maintaining branch coverage at or above 95%
- no lines are manually skipped in coverage calculations

Changes are required to make a best effort to keep or increase coverage before being accepted, but decreases are allowed if properly justified and accepted by reviewers.

Current coverage statistics can be viewed here: [coverage report](https://ci.ros2.org/job/ci_linux_coverage/55/cobertura/ament_index_python/)

### Performance

`ament_index_python` follows the recommendations for performance testing of Python code in the [ROS 2 Developer Guide](https://index.ros.org/doc/ros2/Contributing/Developer-Guide/#performance), and opts to do performance analysis on each release rather than each change.

TODO Will this package require performance testing.

### Linters and Static Analysis

`ament_index_python` uses and passes all the standard linters and static analysis tools for a Python package as described in the [ROS 2 Developer Guide](https://index.ros.org/doc/ros2/Contributing/Developer-Guide/#linters-and-static-analysis). This includes using ament_pep257 and ament_flake8 packages to analyze the code.

TODO any qualifications on what "passing" means for certain linters

## Dependencies

`ament_index_python` has no run-time or build-time dependencies that need to be considered for this declaration.

## Platform Support

`ament_index_python` supports all of the tier 1 platforms as described in [REP-2000](https://www.ros.org/reps/rep-2000.html#support-tiers), and tests each change against all of them.

TODO make additional statements about non-tier 1 platforms?