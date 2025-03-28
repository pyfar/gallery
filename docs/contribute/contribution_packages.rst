.. highlight:: shell

=======================
Contribute to a Package
=======================

These are the pyfar-wide contributing guidelines. For package specific guidelines please visit the documentation for that package, which is linked from *Docs* buttons on `pyfar.org <https://pyfar.org>`_

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


Testing Guidelines
-----------------------
Pyfar uses test-driven development based on `three steps <https://martinfowler.com/bliki/TestDrivenDevelopment.html>`_ and `continuous integration <https://en.wikipedia.org/wiki/Continuous_integration>`_ to test and monitor the code.
In the following, you'll find a guideline. Note: these instructions are not generally applicable outside of pyfar.

- The main tool used for testing is :doc:`pytest<pytest:index>`.
- All tests are located in the *tests/* folder and can by executed with the `pytest` command.
- Make sure that all important parts of pyfar are covered by the tests. This can be checked using *coverage* (see below).
- In case of pyfar, mainly **state verification** is applied in the tests. This means that the outcome of a function is compared to a desired value (``assert ...``). For more information, it is refered to `Martin Fowler's article <https://martinfowler.com/articles/mocksArentStubs.html>`_.

Required Tests
~~~~~~~~~~~~~~

The testing for functions and classes should at least contain tests for

- all errors and warnings (see also function and class guidelines above).
- all input and output parameters.
- specific input and output parameter combinations (if required).
- single and multi-dimensional input data such Signal objects and array likes.
- audio objects with complex time data and NaN values (if applicable).

In case of deprecations, it must also be tested if the deprecated feature is properly removed (see `tests/test_deprecations.py` for examples).

Testing plot functions
~~~~~~~~~~~~~~~~~~~~~~~~~~

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

Tips
~~~~~~~~~~~
Pytest provides several, sophisticated functionalities which could reduce the effort of implementing tests.

- Similar tests executing the same code with different variables can be :doc:`parametrized<pytest:example/parametrize>`. An example is ``test_read_sofa_filename_and_path_object`` in *test_io.py*.

- Run a single test with

    $ pytest tests/test_plot.py::test_line_plots

- Exclude tests (for example the time consuming test of plot) with

    $ pytest -k 'not plot and not interaction'

- Create an html report on the test :doc:`coverage<coverage:index>` with

    $ pytest --cov=. --cov-report=html

- Feel free to add more recommendations on useful pytest functionalities here. Consider, that a trade-off between easy implemention and good readability of the tests needs to be found.

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


Writing the Documentation
-------------------------

Pyfar follows the :doc:`numpy style guide<numpydoc:format>` for the docstring. A docstring has to consist at least of

- a short and/or extended summary,
- the Parameters section, and
- the Returns section.

Optional fields that are often used are

- References,
- Examples, and
- Notes.

Here are a few tips to make things run smoothly.

- Use the tags ``:py:func:``, ``:py:mod:``, and ``:py:class:`` to reference functions, modules, and classes from the package itself: For example ``:py:func:`~pyfar.plot.time``` for a link that displays only the function name. For links with custom text use ``:py:mod:`plot functions <pyfar.plot>```.
- Code snippets and values as well as external modules, classes, functions are marked by double ticks \`\` to appear in mono spaced font, e.g., ``x=3`` or ``pyfar.Signal``.
- Parameters, returns, and attributes are marked by single ticks \` to appear as emphasized text, e.g., *unit*.
- Use ``[#]_`` and ``.. [#]`` to get automatically numbered footnotes.
- Do not use footnotes in the short summary. Only use footnotes in the extended summary if there is a short summary. Otherwise, it messes with the auto-footnotes.
- If a method or class takes or returns pyfar objects defined in the package for example write ``parameter_name : Signal``. This will create a link to the ``pyfar.Signal`` class.
- If a method or class takes or returns pyfar objects from other packages for example write ``parameter_name : :py:class:`~pyfar.classes.audio.Signal``` to create the link. Note that this requires an intersphinx mapping in `docs/conf.py` in this case ``intersphinx_mapping = {'pyfar': ('https://pyfar.readthedocs.io/en/stable/', None)}``.
- you can refer to the gallery notebooks using ``:doc:`gallery:gallery/interactive/pyfar_audio_objects```. A section of a notebook can be referenced using ``:ref:`gallery:/gallery/interactive/fast_fourier_transform.ipynb#fft-normalizations```.
- you can use ``python -m sphinx.ext.intersphinx https://pyfar-gallery.readthedocs.io/en/latest/objects.inv > mapping.txt`` to write the mapping for e.g. gallery into a textfile.
- note that sphinx links should be used everywhere except within gallery notebooks.
- Plots can be included in the documentation by using the prefix ``.. plot::`` followed by an empty line and an indented block containing the code for the plot. See `pyfar.plot.line.time.py` for examples.

See the `Sphinx homepage <https://www.sphinx-doc.org>`_ for more information.

Building the Documentation
--------------------------

You can build the documentation of your branch using Sphinx by executing the make script inside the docs folder.

.. code-block:: console

    $ cd docs/
    $ make html -j

The ``-j`` option uses multiple cores to speed up the build process in Linux and Mac. After Sphinx finishes you can open the generated html using any browser.

.. code-block:: console

    $ docs/_build/index.html

Note that some warnings are only shown the first time you build the
documentation. To show the warnings again use

.. code-block:: console

    $ make clean

before building the documentation.


Deploying
---------

A reminder for the maintainers on how to deploy.

- Commit all changes to develop.
- Update HISTORY.rst in develop.
- Merge develop into main.

Switch to main to update the version::

$ bump-my-version bump patch --verbose  # possible version bumps: major / minor / patch
$ git push --follow-tags

The testing platform will then deploy to PyPI if tests pass.

- Merge main back into develop.
