Documentation Guidelines
------------------------

Pyfar follows the :doc:`numpy style guide<numpydoc:format>` for the docstring. A docstring has to consist at least of

- a short and/or extended summary,
- the *Parameters* section, and
- the *Returns* section.

Optional fields that are often used are

- *References*,
- *Examples*, and
- *Notes*.

Here are a few tips to make things run smoothly.

- Use the tags ``:py:func:``, ``:py:mod:``, and ``:py:class:`` to reference functions, modules, and classes from the package itself. For example ``:py:func:`~pyfar.plot.time``` for a link that displays only the function name, for links with custom text use ``:py:mod:`plot functions <pyfar.plot>```.
- Code snippets and values as well as external modules, classes, functions are marked by double ticks \`\` to appear in mono spaced font, e.g., ``x=3`` or ``pyfar.Signal``.
- Parameters, returns, and attributes are marked by single ticks \` to appear as emphasized text, e.g., *unit*.
- Use ``[#]_`` when citing and ``.. [#]`` in the *References* field to get automatically numbered footnotes.
- Do not use footnotes in the short summary. Only use footnotes in the extended summary if there is a short summary. Otherwise, it messes with the auto-footnotes.
- If a method or class takes or returns pyfar objects defined in the package for example write ``parameter_name : Signal``. This will create a link to the ``pyfar.Signal`` class.
- If a method or class takes or returns pyfar objects from other packages for example write ``parameter_name : :py:class:`~pyfar.classes.audio.Signal``` to create the link. Note that this requires an intersphinx mapping in `docs/conf.py` in this case ``intersphinx_mapping = {'pyfar': ('https://pyfar.readthedocs.io/en/stable/', None)}``.
- You can refer to the gallery notebooks using ``:doc:`gallery:gallery/interactive/pyfar_audio_objects```. A section of a notebook can be referenced using ``:ref:`gallery:/gallery/interactive/fast_fourier_transform.ipynb#fft-normalizations```.
- You can use ``python -m sphinx.ext.intersphinx https://pyfar-gallery.readthedocs.io/en/latest/objects.inv > mapping.txt`` to write the mapping for e.g. gallery into a textfile.
- Note that sphinx links should be used everywhere except within gallery notebooks.
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

    $ _build/html/index.html

If the documentation is rebuilt a second time, Sphinx will simply re-build the changes.
As a result, some warnings appear only during the first build.
To reset the build, run

.. code-block:: console

    $ make clean

before re-building the documentation.
