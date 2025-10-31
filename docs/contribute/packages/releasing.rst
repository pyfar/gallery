Release Guidelines
------------------

Versioning
==========

Pyfar uses the `Semantic Versioning <https://semver.org>`_ scheme.
This means that version numbers are of the form ``MAJOR.MINOR.PATCH``.

In short, this means the following:

- MAJOR version when you make incompatible API changes
- MINOR version when you add functionality in a backward compatible manner
- PATCH version when you make backward compatible bug fixes

If unsure, please refer to the `Semantic Versioning`_ documentation for details.

PRs falling into the PATCH category are made against the main branch (and consequently need a branch off main),
while MINOR and MAJOR changes are made against the develop branch (and consequently need a branch off develop).
Note that PRs that only change documentation or examples are considered PATCH changes.
Updates to the CI configuration or similar infrastructure which do not affect the API
are not considered for version increments.


Release Workflow
================

A reminder for the maintainers on how to release a new version.

Prepare the release
~~~~~~~~~~~~~~~~~~~

When preparing for a new major or minor release, please merge the develop branch into main.
Patch releases are directly made on the main branch without merging from develop.
The following steps are then required to prepare a new release:

- Update the changelog in HISTORY.rst.
- Commit all required changes.
- Run the test suite and ensure that all tests pass.
- Build the documentation and check that it builds without errors.

Incrementing the version number
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pyfar uses `bump-my-version <https://pypi.org/project/bump-my-version/>`_ to manage version numbers.

To increment the version number (can be major, minor, or patch), run the following commands:

.. code-block:: console

   $ bump-my-version bump patch --verbose


This will update the version number in all required files and create a git tag for the new version.
The --verbose flag will output all files that were changed.

Publishing the new version
~~~~~~~~~~~~~~~~~~~~~~~~~~

Finally, the tag needs to be pushed to the remote repository via:

.. code-block:: console

   $ git push --follow-tags


Afterwards, the test suite will automatically be run remotely on CircleCI.
If all tests pass, the new version will be published to PyPI using CircleCI.


Post-release steps
~~~~~~~~~~~~~~~~~~

After the release is published, please make sure to merge the main branch back into develop.

Don't forget to announce the new release through the pyfar Slack channel
and give a cheer to the community for their contributions.