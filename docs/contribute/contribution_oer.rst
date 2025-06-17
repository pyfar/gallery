============================================
Contribute to the Open Educational Resources
============================================


The collection of open educational resources is organized across two different repositories:
A repository containing all assignments including the solutions and a repository containing only the assignments.
Please understand that the repository containing the solutions is not publicly available.
To avoid mismatches between the public assignments and solutions, the assignments are created from the private repository and pushed to the public repository.
This process of creating the assignments from the notebooks including solutions is automated using the nbgrader package.
As the name implies, nbgrader can also be used to (at least partially) automate grading the assignments.
For an introduction to nbgrader, please refer to the `nbgrader documentation <https://nbgrader.readthedocs.io/en/stable/>`_.
If you want to contribute to the open educational resources, please first get in touch with us to get access to the private repository.
Ways to contact us are listed :doc:`here<index>`.

Get Started
-----------

Ready to contribute? Here's what you need to do:

After getting in touch with us you should now have access to the closed-educational-resources
repository on GitHub. This is the repository where the assignments including the solutions are
stored.

1. `Fork <https://docs.github.com/en/get-started/quickstart/fork-a-repo/>`_ the `closed-educational-resources <https://github.com/pyfar/closed-educational-resources>`_ repo on GitHub.

2. Clone your fork locally and cd into the root directory:

.. code-block:: shell

    git clone https://github.com/YOUR_USERNAME/closed-educational-resources.git
    cd closed-educational-resources

1. Install your local copy into a virtualenv. Assuming you have Anaconda or Miniconda installed, this is how you set up your fork for local development:

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

Now you can create your assignment locally. For a detailed guide on how to
create assignments, please refer to :ref:`Creating an Assignment<creating-an-assignment>`.

6. Commit your changes and push your branch to GitHub. Commit only the core assignment files.
   Avoid committing supplementary, generated, or temporary files.
   Please refer to the :ref:`File Handling<file-handling>` section for more information.

.. code-block:: shell

    git add .
    git commit -m "Your detailed description of your changes."
    git push origin course1/assignment1

7. Submit a pull request on the main branch through the GitHub website.


Repository Structure
--------------------

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

To create a new course, add a folder in the ``courses`` directory and name it
after your course (e.g., ``course1``).
This course directory is where all solution notebooks, the nbgrader config, etc., are stored.
Every course requires an ``nbgrader_config.py`` file. Please refer to the
course_exmaple on closed-educational-resources and the
`nbgrader configuration documentation <https://nbgrader.readthedocs.io/en/latest/configuration/nbgrader_config.html>`_,
there are alot of configuraiton options available.

.. _creating-an-assignment:

Creating an Assignment
----------------------

This course folder serves as the root directory from which nbgrader runs to generate
new release notebooks. Newly added notebooks must be stored in their respective
assignment folder inside the ``source`` directory. This is where nbgrader looks
for assignments by default.

If you are creating a new course, add a ``source`` folder inside the course directory.
Then, create a subfolder for your assignment (e.g., ``assignment1``).
This assignment folder can contain multiple notebooks (e.g., ``problem1``, ``problem2``).
All notebooks within an assignment should be thematically related — for example,
covering material from a single class session on one topic within the lecture series.
If the notebooks cover unrelated topics, it's recommended to create separate assignments.

You can also add assignments in an existing course. To do so, just add a new
assignment folder inside the ``source`` directory of the course.

We use ``nbgrader`` to generate the release version of the assignments. This happens
automatically in circleci / GitHub Actions when a :ref:`pull request is submitted<pull-request>`.
The best way to create an nbgrader assignment is to use the `Jupyter notebook
extension <https://nbgrader.readthedocs.io/en/latest/user_guide/highlights.html#instructor-interface>`_.

You can find a `template-notebook <link-to-template>`_ including detailed instructions and guidelines
in the `course example <link-to-example-course>`_. This exmaple course serves
as a template for your assignment.


To check the release version of your assignment locally, you can run

.. code-block:: shell

    nbgrader generate_assignment <assignment_name>

in your course directory. This will generate the release version in a new
``release`` folder. Make sure not to push release versions to the repository.

.. _file-handling:

File Handling
-------------

To prevent large supplementary files in the repository, we use
`pooch <https://www.fatiando.org/pooch/latest/>`_ to handle the downloading of
files when a notebook is executed.
These files can be stored in the pyfar `files-repository <https://github.com/pyfar/files>`_

A detailed guide on how to use pooch is also available in the `template-notebook <link-to-template>`_.

.. _pull-request:

Pull Request & GitHub Workflow
------------------------------

Once you pushed your local changes to GitHub, you can submit a pull request to
the main branch of the closed-educational-resources repository.

Given everything is set up correctly, a circleci-workflow will generate a
html preview of the release-version of your assignment. You can access this
rendered html via the artifacts of the ``generate_release_and_build_docs`` workflow.

Once formally reviewed and approved, you can assign the label "ready to merge"
to your pull request. This will trigger a workflow that creates a pull request
on the public `open-educational-resources <https://github.com/pyfar/open-educational-resources>`_ repository, adding the release version
of your assignment.

On the open-educational-resources pull request you have to add a thumnbail and adjust
the docs (e.g. correct affiliation of your assignment to a course).

Once this pull-request is reviewed and approved, it will be merged into the
main branch and then be publicly available on `pyfar open educational resources <https://pyfar-oer.readthedocs.io/en/latest/open_educational_resources.html>`_.

Licensing
---------
Unless otherwise stated the notebooks are released under © 2024 by `the pyfar developers <https://github.com/orgs/pyfar/people>`_ are licensed under `CC BY 4.0 <http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1>`_.
If required, a different but compatible license can be chosen for single notebooks.
Simply adapt the author name and license information in the respective section at the end of the notebook.
Note that if a notebook contains code or content from other sources, this should be clearly stated in the notebook.
