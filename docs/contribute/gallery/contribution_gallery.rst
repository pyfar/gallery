=========================
Contribute to the Gallery
=========================

Get Started
-----------

Ready to contribute? Here's how to set up `pyfar_gallery` for local development using the command-line interface. Note that several alternative user interfaces exist, e.g., the Git GUI, `GitHub Desktop <https://desktop.github.com/>`_, extensions in `Visual Studio Code <https://code.visualstudio.com/>`_ ...

1. `Fork <https://docs.github.com/en/get-started/quickstart/fork-a-repo/>`_ the `gallery` repo on GitHub.
2. Clone your fork locally and cd into the gallery directory:

.. code-block:: shell

    git clone https://github.com/YOUR_USERNAME/gallery.git
    cd gallery

3. Install your local copy into a virtualenv. Assuming you have Anaconda or Miniconda installed, this is how you set up your fork for local development:

.. code-block:: shell

    conda create --name gallery python
    conda activate gallery
    pip install -r requirements.txt


4. You will also require pandoc. If you don't have it installed, you can download it from the `official website <https://pandoc.org/installing.html>`_. Alternatively, you can install it using conda using the conda-forge channel:

.. code-block:: shell

    conda install -c conda-forge pandoc


5. Set up pre-commit hooks. This will cause commits to fail and clean all notebooks if the notebooks in `docs/gallery/interactive` aren't cleaned from outputs. After that, the automatic changes can be added and committed:

.. code-block:: shell

    pre-commit install

6. Create a branch for local development. Indicate the intention of your branch in its respective name (i.e. `feature/branch-name` or `bugfix/branch-name`):

.. code-block:: shell

    git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

7. Commit your changes and push your branch to GitHub:

.. code-block:: shell

    git add .
    git commit -m "Your detailed description of your changes."
    git push origin name-of-your-bugfix-or-feature

8. Submit a pull request on the develop branch through the GitHub website.

Structure
---------

The gallery is separated into *interactive* and *static* notebooks, allowing to include notebooks for which execution on readthedocs or CircleCI is not feasible.
This could be due to the need for specific hardware, such as audio interfaces or other io-devices, as well as notebooks with very long execution times or computational demands.

To add notebooks to the gallery, simply place them inside ``docs/gallery/interactive`` or ``docs/gallery/static``, respectively.
Note that all notebooks added to the folder ``interactive`` should not contain output for any of the cells, see the section above for setting up the pre-commit hooks to automatically clean the notebooks from outputs,

A very bare template for new notebooks is provided in `docs/contribute/template.ipympl <template.html>`_. It is highly recommended to use it for consistency with other notebooks.

.. code-block:: shell

    docs
    ├── Makefile
    ├── _build
    ├── _templates
    │   └── template.ipynb
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

Note that notebooks placed in the static folder omitted from unit testing on CircleCI and hence need appropriate offline testing.
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

       gallery/interactive/your_new_notebook.ipynb

Licensing
---------
Unless otherwise stated the notebooks are released under © 2024 by `the pyfar developers <https://github.com/orgs/pyfar/people>`_ are licensed under `CC BY 4.0 <http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1>`_.
If required, a different but compatible license can be chosen for single notebooks.
Simply adapt the author name and license information in the respective section at the end of the notebook.
Note that if a notebook contains code or content from other sources, this should be clearly stated in the notebook.
