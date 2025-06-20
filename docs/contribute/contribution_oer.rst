============================================
Contribute to the Open Educational Resources
============================================


The collection of open educational resources is organized across two different repositories:
A private repository containing all assignments including the solutions and a public repository containing only the assignments.

The assignments are created on the private repository and automatically pushed to the public repository after they have been reviewed.
The following steps guide you through adding your first assignment and publishing it on `pyfar.org <https://pyfar.org>`_.
If you want to contribute to the open educational resources, please first :doc:`get in touch <index>` with us to get access to the private repository.

1. Get Started
--------------

Ready to contribute? Here's what you need to do:

After getting in touch with us you should now have access to the closed-educational-resources
repository on GitHub. This is the repository where the assignments including the solutions are
stored.

1. `Fork <https://docs.github.com/en/get-started/quickstart/fork-a-repo/>`_ the `closed-educational-resources <https://github.com/pyfar/closed-educational-resources>`_ repo on GitHub.

2. Clone your fork locally and cd into the root directory:

.. code-block:: shell

    git clone https://github.com/YOUR_USERNAME/closed-educational-resources.git
    cd closed-educational-resources

3. Install your local copy into a virtualenv. Assuming you have Anaconda or Miniconda installed, this is how you set up your fork for local development:

.. code-block:: shell

    conda create --name cer python
    conda activate cer
    pip install ".[dev]"


4. You will also require pandoc. If you don't have it installed, you can download it from the `official website <https://pandoc.org/installing.html>`_. Alternatively, you can install it using conda using the conda-forge channel:

.. code-block:: shell

    conda install -c conda-forge pandoc

5. Create a local branch for your assignment. Indicate the course and assignment in the branch-name (e.g. `course1/assignment1`):

.. code-block:: shell

    git checkout -b course1/assignment1

Now you can create your assignment locally.


.. _creating-an-assignment:

2. Create an Assignment
-------------------------

To create an assignment for a new course, you can use the `course example <https://github.com/pyfar/closed-educational-resources/tree/main/course_example>`_
as a template. This example provides the necessary structure to get your
assignment running with the workflows on closed-educational-resources. It also
contains a `template-notebook <https://github.com/pyfar/closed-educational-resources/blob/main/course_example/source/assignment1/template.ipynb>`_
with detailed instructions.

To start your course / assignment:

1. Copy ``course_example`` folder to the ``courses`` directory.
2. Rename according to your course / institution (check `existing courses <https://github.com/pyfar/closed-educational-resources/tree/main/courses>`_
   for examples). Make sure to also adjust the ``course_id`` in
   ``nbgrader_config.py``.
3. Rename assignment folder according to your topic.
4. Open the example notebook in your editor of choice and follow the contained
   guidelines to create your assignment.

.. note::

   If you want to add an assignment to an existing course, just add a new
   assignment folder to the course's ``source`` directory.

.. _pull-request:

3. Create a Pull Request
------------------------

Commit your changes and push your branch to GitHub. Commit only the core assignment
files. Please refer to the file handling section of the `template-notebook <https://github.com/pyfar/closed-educational-resources/blob/main/course_example/source/assignment1/template.ipynb>`_
for more information.

.. note::

   Avoid committing supplementary, generated, or temporary files. Also don't push
   any ``.db``-files to the repository, they might contain sensitive information
   on students.

.. code-block:: shell

   git add .
   git commit -m "Your detailed description of your changes."
   git push origin course1/assignment1

Once you pushed your local changes to GitHub, you can submit a pull request to
the main branch of the closed-educational-resources repository.

Given everything is set up correctly, you can access an html-preview of the release
version via the artifacts of the ``generate_release_and_build_docs`` workflow.

Now your assignment needs to be reviewed by other members of the group.

4. Publish the assignment
-------------------------

Once formally reviewed and approved, the pyfar developers will create a pull
request on the public `open-educational-resources <https://github.com/pyfar/open-educational-resources>`_
repository, adding the release version of your assignment.

There you can give your assignment a final check and adjust thumnbail and docs
(e.g. correct affiliation of your assignment to a course).

Once this pull request is approved, the pyfar developers will publish your
assignment.

Additional Information
----------------------

If you follow the instructions above and in the template-notebook you should
be able to create your assignment without any problems. If you need more
information or run into issues, the section below might help.

Repository Structure
~~~~~~~~~~~~~~~~~~~~

Infrastructure and workflow in this repository follow the
`nbgrader folder structure <https://nbgrader.readthedocs.io/en/latest/user_guide/philosophy.html>`_.

.. code-block:: text

    closed-educational-resources/
    ├── courses/
    │   ├── course1/
    │   │   ├── nbgrader_config.py
    │   │   └── source/
    │   │       └── assignment1/
    │   │           └── problem1.ipynb
    │   ├── course2/
    │   │   ├── nbgrader_config.py
    │   │   └── source/
    │   │       └── assignment1/
    │   │           ├── problem1.ipynb
    │   │           └── problem2.ipynb
    │   └── ...

The course directory is where all solution notebooks, the nbgrader config, etc., are stored.
Every course requires an ``nbgrader_config.py`` file. Please refer to the
`course_example <https://github.com/pyfar/closed-educational-resources/tree/main/course_example>`_
on closed-educational-resources and the
`nbgrader configuration documentation <https://nbgrader.readthedocs.io/en/latest/configuration/nbgrader_config.html>`_,
there are a lot of configuration options available.

The course folder serves as the root directory from which nbgrader runs to generate
new release notebooks. Newly added notebooks must be stored in their respective
assignment folder inside the ``source`` directory. This is where nbgrader looks
for assignments by default.

A course contains a ``source`` folder and subfolders for the assignments.
An assignment folder can contain multiple notebooks (e.g., ``problem1``, ``problem2``).
All notebooks within an assignment should be thematically related — for example,
covering material from a single class session on one topic within the lecture series.
If the notebooks cover unrelated topics, it's recommended to create separate assignments.

Nbgrader
~~~~~~~~

We use ``nbgrader`` to generate the release version of the assignments. This happens
automatically in circleci / GitHub Actions when a pull request is submitted.
The best way to create an nbgrader assignment is to use the `Jupyter notebook
extension <https://nbgrader.readthedocs.io/en/latest/user_guide/highlights.html#instructor-interface>`_.

To check the release version of your assignment locally, you can run

.. code-block:: shell

    nbgrader generate_assignment <assignment_name>

in your course directory. This will generate the release version in a new
``release`` folder. Make sure not to push release versions to the repository.

Html-preview
~~~~~~~~~~~~

The open-educational-resources are built using `Sphinx <https://www.sphinx-doc.org/en/master/index.html>`_.
To locally build the docs to check the html version of your assignment, copy
your assignment to ``open-educational-resources/oer/docs`` and run

.. code-block:: shell

   make html

with the docs folder as root. This starts the docs build. You can find the
generated docs inside the ``build`` directory, including your
``notebook.html``.

Licensing
---------
Unless otherwise stated the notebooks are released under © 2024 by `the pyfar developers <https://github.com/orgs/pyfar/people>`_ are licensed under `CC BY 4.0 <http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1>`_.
If required, a different but compatible license can be chosen for single notebooks.
Simply adapt the author name and license information in the respective section at the end of the notebook.
Note that if a notebook contains code or content from other sources, this should be clearly stated in the notebook.

