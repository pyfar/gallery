.. highlight:: shell

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put your new functionality into a function with a docstring.
3. If checks do not pass, have a look at https://app.circleci.com/pipelines/github/pyfar/PACKAGENAME for more information (e.g., use 'pyfar' as the PACKAGENAME).

Function and Class Guidelines
-----------------------------

Functions and classes should

* have a single clear purpose and a functionality limited to that purpose. Conditional parameters are fine in some cases but are an indicator that a function or class does not have a clear purpose. Conditional parameters are

  - parameters that are obsolete if another parameter is provided
  - parameters that are necessary only if another parameter is provided
  - parameters that must have a specific value depending on other parameters

* be split into multiple functions or classes if the functionality is not well limited.
* contain documentation for all input and output parameters.
* contain examples in the documentation if they are non-trivial to use.
* contain comments in the code that explain decisions and parts that are not trivial to read from the code.
* use unique and descriptive names for all variables.

It is also a good idea to follow `the Zen of Python <https://peps.python.org/pep-0020/>`_.

Errors should be raised if

* audio objects do not have the correct type (e.g. a TimeData instance is passed but a Signal instance is required).
* string input that specifies a function option has an invalid value (e.g. 'linea' was passed but 'linear' was required).
* invalid parameter combinations are used.

Warnings should be raised if

* results might be wrong or unexpected.
* possibly invalid parameter combinations are used.
* features are deprecated.