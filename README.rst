=============
pyfar gallery
=============

.. image:: https://readthedocs.org/projects/pyfar-gallery/badge/?version=latest
    :target: https://pyfar-gallery.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status
.. image:: https://circleci.com/gh/pyfar/gallery.svg?style=shield
    :target: https://circleci.com/gh/pyfar/gallery
.. image:: https://mybinder.org/badge_logo.svg
    :target: https://mybinder.org/v2/gh/pyfar/gallery/main?filepath=docs/gallery


This is the pyfar gallery. It contains examples of applications pyfar and its sub-packages can be used for.
Each of the notebooks in the gallery has a `binder`_ link to start an interactive jupyter session.
The rendered version of the gallery is hosted on `readthedocs.org`_.


.. _binder: https://mybinder.org/v2/gh/pyfar/gallery/main?filepath=docs/gallery
.. _readthedocs.org: https://pyfar-gallery.readthedocs.io/en/latest



============
Contributing
============

The gallery is separated into *interactive* and *static* notebooks, allowing to include notebooks for which execution on readthedocs or CircleCI is not feasible.
This could be due to the need for specific hardware, such as audio interfaces or other io-devices, as well as notebooks with very long execution times or computational demands.


To add notebooks to the gallery, simply place them inside ``docs/gallery/interactive`` or ``docs/gallery/static``, respectively.

.. code-block:: shell

    docs
    ├── Makefile
    ├── _build
    ├── _templates
    ├── _static
    ├── conf.py
    ├── gallery
    │   ├── interactive
    │   │   ├── your_new_notebook.ipynb
    │   │   └── interactive_demo.ipynb
    │   └── static
    │       └── pre_executed_notebook.ipynb
    ├── index.rst
    ├── make.bat
    └── resources

Metadata for static notebooks
-----------------------------

Note that notebooks placed in the static folder omitted from unit testing on CircleCI and hence need apprpriate offline testing.
Static notebooks further need to include the setting

.. code-block:: json

    "nbsphinx": {
        "execute": "never"
    },

as part of their JSON meta-data.
For more information see the `nbsphinx documentation <https://nbsphinx.readthedocs.io/en/latest/never-execute.html>`_

Thumbnails
----------

Nbspinx does select the last output of a notebook as thumbnail by default.
If a specific output from a notebook should be selected as thumbnail, the meta data of the cell containing the output must be tagged

.. code-block:: json

    "metadata": {
        "nbsphinx-thumbnail": {}
    }

If the notebook contains no output, a thumbnail can be added by placing a file in the ``docs/gallery/_static`` folder.
The filename and notebook name need to be added to the ``nbspinx_thumbnails`` dictionary in the ``conf.py`` file.

.. code-block:: python

    sphinx_thumbnails = {
        'gallery/interactive/your_new_notebook': '_static/thumbnail_added.png',
    }

The respective file tree for this example would look like this:

.. code-block:: shell

    docs
    ├── Makefile
    ├── _build
    ├── _static
    │   └── thumbnail_added.png
    ├── conf.py
    ├── gallery
    │   ├── interactive
    │   │   └── your_new_notebook.ipynb


Adding a notebook to the gallery
--------------------------------

Finally, add the notebook to an appropriate ``nbgallery`` inside the ``docs/index.rst``. For example:

.. code-block:: rst

    .. nbgallery::
       :caption: Getting Started
       :name: pyfar_gallery
       :glob:
       :reversed:

       gallery/interactive/pyfar_demo.ipynb
       gallery/interactive/your_new_notebook.ipynb
