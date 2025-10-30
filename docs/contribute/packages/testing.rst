Testing Guidelines
------------------

All pyfar packages are required to include tests for their code. These are intended to

- Ensure that the code works as intended and bugs are detected early.
- Avoid that future changes to the code do not unintentionally break existing functionality.
- Provide additional definitions of the intended behavior and use-cases of the code.
- Ensure that code produces consistent results when with different or updated versions of dependencies.

The tests should always be run locally before opening a pull request. In addition, all tests are automatically executed by continuous integration services when a pull request is opened (see the `respective guidelines <../general/pr_workflow.html>`_ for more information).

In the following, you'll find a guideline. Note: these instructions are not generally applicable outside of pyfar.

- The main tool used for testing is :doc:`pytest<pytest:index>`.
- All tests are located in the *tests/* folder and can by executed with the ``pytest`` command.
- Make sure that all important parts of pyfar are covered by the tests. This can be checked using *coverage* (see below).
- In case of pyfar, mainly **state verification** is applied in the tests. This means that the outcome of a function is compared to a desired value (``assert ...``). For more information, it is refered to `Martin Fowler's article <https://martinfowler.com/articles/mocksArentStubs.html>`_.

Best Practices
~~~~~~~~~~~~~~

Please consider the following aspects when writing tests:

- Pyfar generally uses  **unit tests** to test small parts of the code in isolation. This agrees very well with the code design guidelines of writing compact and modular code (see the `style guidelines <style_design.html>`_).
- Tests should be easy to read and understand. This includes

  - Meaningful test names, comments, and a clear structure of the test code.
  - Writing separate tests for different functionalities instead of combining all checks in a single test.
  - Avoid conditional statements and loops within tests if possible.

- Keep tests independent of each other. Each test should be able to run in isolation without relying on the outcome of other tests.
- Use **fixtures** to set up common test data or state. This avoids code duplication and improves readability. See the `Fixtures`_ section below for more information.
- Note that the modular and compact `code design guidelines <style_design.html>`_ and unit-testing usually go hand in hand: If the code is not concise and compact, writing a compact unit test is (more) difficult. It might be worth to reconsider the code design in this case.
- Keep tests fast to run. This encourages frequent execution of the tests during development and avoids long waiting times for continuous integration services.
- Aim for high **code coverage**. Note that a 100% coverage is not always achievable or necessary. Use a `coverage` tool to check the coverage of your tests.
- Pyfar recommends test-driven development based on `three steps <https://martinfowler.com/bliki/TestDrivenDevelopment.html>`_.


Required Tests
~~~~~~~~~~~~~~

The testing for functions and classes should at least contain tests for

- all errors and warnings (see also function and class guidelines above).
- all input and output parameters.
- specific input and output parameter combinations (if required).
- single and multi-dimensional input data such Signal objects and array likes.
- audio objects with complex time data and NaN values (if applicable).

In case of deprecations, it must also be tested if the deprecated feature is properly removed (see `tests/test_deprecations.py` for examples).

Tips
----

Running tests locally with pytest
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Python projects use `pytest <https://docs.pytest.org/en/stable/>`_ as testing framework.
To run all tests within a project, simply execute the following command in the terminal from the root folder of the project:

.. code-block:: shell

   $ pytest

Pytest provides several, sophisticated functionalities which could reduce the effort of implementing tests.

- Similar tests executing the same code with different variables can be :doc:`parametrized<pytest:example/parametrize>`. An example is ``test_read_sofa_filename_and_path_object`` in *test_io.py*.

- Run a single test with

.. code-block:: shell

   $ pytest tests/test_plot.py::test_line_plots

- Exclude tests (for example the time consuming test of plot) with

.. code-block:: shell

   $ pytest -k 'not plot and not interaction'

- Create an html report on the test :doc:`coverage<coverage:index>` with

.. code-block:: shell

   $ pytest --cov=. --cov-report=html

- Feel free to add more recommendations on useful pytest functionalities here. Consider, that a trade-off between easy implemention and good readability of the tests needs to be found.

Testing plot functions
~~~~~~~~~~~~~~~~~~~~~~

The above also holds for plot functions, however, in this case it is required that the tests generate baseline and test images. The following documents the current best practice. See below for a code example.

Baseline images show how an image produced by a given plot command (for example `pf.plot.time(pf.Signal[0, 1, 0], 1)`) should look like. Baseline images must be created when a new plot function or test is introduced, and they must be overwritten when the behavior of a plot function changes, e.g., because of a bug fix. Baseline images must be visually inspected as part of a pull request when they are created or changed.

Test images show how an image produced by a given plot function in the testing environment looks like. Test images must be created each time the tests run. If the behavior of a plot function changes, the corresponding test image will change. In this case, the changed test image must be visually compared to the corresponding baseline image as part of a pull request.

``pyfar.testing.plot_utils`` contains the function ``create_figure`` for creating a figure in a way that produces almost identical results across operating systems. This follows the Matplotlib best practice. The function ``save_and_compare`` can save and compare test plots to the baseline automatically. The automatic comparison is best practice recommended by Matplotlib, however, it is usually disabled. It often fails because the plots generated by Matplotlib depend on the operating system. Different operating systems create offsets of a few pixels resulting in large differences in numerical error estimates between test and baseline plots.

.. code-block:: python

    import pyfar as pf
    from pyfar.testing.plot_utils import create_figure, save_and_compare

    # should manually be set to `True` if and only if the baseline changed
    create_baseline = False

    # Comparing the output should be disabled (see above for why)
    compare_output = False

    def test_plot_function():

        create_figure()
        pf.plot.time(pf.Signal([0, 1, 0], 1))
        save_and_compare(
            create_baseline, 'path_to/baseline_folder/baseline_image',
            'path_to/test_folder', 'test_image',
            file_type='png', compare_output=compare_output)

Fixtures
~~~~~~~~
"Software test fixtures initialize test functions. They provide a fixed baseline so that tests execute reliably and produce consistent, repeatable, results. Initialization may setup services, state, or other operating environments. These are accessed by test functions through parameters; for each fixture used by a test function there is typically a parameter (named after the fixture) in the test function’s definition." (from :doc:`pytest fixtures<pytest:explanation/fixtures>`)

- All fixtures are implemented in *conftest.py*, which makes them automatically available to all tests. This prevents from implementing redundant, unreliable code in several test files.
- Typical fixtures are pyfar objects with varying properties, stubs as well as functions need for initiliazing tests.
- Define the variables used in the tests only once, either in the test itself or in the definition of the fixture. This assures consistency and prevents from failing tests due to the definition of variables with the same purpose at different positions or in different files.

Have a look at already implemented fixtures in *confest.py*.

**Dummies**

If the objects used in the tests have arbitrary properties, tests are usually better to read, when these objects are initialized within the tests. If the initialization requires several operations or the object has non-arbitrary properties, this is a hint to use a fixture.
Good examples illustrating these two cases are the initializations in *test_signal.py* vs. the sine and impulse signal fixtures in *conftest.py*.

**Stubs**

Stubs mimic actual objects, but have minimum functionality and **fixed, well defined properties**. They are **only used in cases, when a dependence on the actual pyfar class is prohibited**. This is the case, when functionalities of the class itself or methods it depends on are tested. Examples are the tests of the Signal class and its methods in *test_signal.py* and *test_fft.py*.

It requires a little more effort to implement stubs of the pyfar classes. Therefore, stub utilities are provided in *pyfar/testing/stub_utils.py* and imported in *confest.py*, where the actual stubs are implemented.

- Note: the stub utilities are not meant to be imported to test files directly or used for other purposes than testing. They solely provide functionality to create fixtures.
- The utilities simplify and harmonize testing within the pyfar package and improve the readability and reliability.
- The implementation as the private submodule ``pyfar.testing.stub_utils``  further allows the use of similar stubs in related packages with pyfar dependency (e.g. other packages from the pyfar family).

**Mocks**

Mocks are similar to stubs but used for **behavioral verification**. For example, a mock can replace a function or an object to check if it is called with correct parameters. A main motivation for using mocks is to avoid complex or time-consuming external dependencies, for example database queries.

- A typical use case of mocks in the pyfar context is hardware communication, for example reading and writing of large files or audio in- and output. These use cases are rare compared to tests performing state verification.
- In contrast to some other guidelines on mocks, external dependencies do **not** need to be mocked in general. Failing tests due to changes in external packages are meaningful hints to modify the code.
- Examples of internal mocking can be found in *test_io.py*, indicated by the pytest ``@patch`` calls.
