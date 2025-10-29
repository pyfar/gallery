.. raw:: html

    <style>
      span.github-green {background-color: #28a745; color: white; padding: 4px 6px; border-radius: 3px;}
      span.github-yellow {background-color: #ffcc00; color: black; padding: 4px 6px; border-radius: 3px;}
      span.github-burgundy {background-color: #981e51ff; color: white; padding: 4px 6px; border-radius: 3px;}
      span.github-purple {background-color: #6f42c1; color: white; padding: 4px 6px; border-radius: 3px;}
      span.github-grey {background-color: #6c757d; color: white; padding: 4px 6px; border-radius: 3px;}
      span.github-red {background-color: #d73a49; color: white; padding: 4px 6px; border-radius: 3px;}
      span.github-blue {background-color: #0366d6; color: white; padding: 4px 6px; border-radius: 3px;}
    </style>


.. role:: approved
   :class: sd-badge pst-badge github-green

.. role:: implementation-in-progress
   :class: sd-badge pst-badge github-yellow

.. role:: open-discussion
   :class: sd-badge pst-badge github-burgundy

.. role:: backlog
   :class: sd-badge pst-badge github-grey

.. role:: require-review
   :class: sd-badge pst-badge github-red

.. role:: drafting-phase
   :class: sd-badge pst-badge github-purple

.. role:: ready-for-pickup
   :class: sd-badge pst-badge github-blue


Development Workflow
====================

All pyfar related projects and packages are developed openly on GitHub.
Contributions are managed through issues and pull requests, allowing communication
between users, developers, and maintainers.
Pull requests can be proposed from forks of the repository for which a contribution
is to be committed.
For contributors who are part of the pyfar organization it is recommended to work on feature
branches on the repository directly.


Workflow in a Nutshell
----------------------

The workflow can very briefly be summarized as:

- Start a new feature branch for each set of edits that you do.
- Hack away!
- Push your feature branch to your own Github repo, and create a pull request.
- Request a review and wait for feedback
- If required, include the feedback from the review and update your code.
- A maintainer will merge your PR if two reviewers approved.

This way of working helps to keep work well organized.

More Detailed Instructions
--------------------------

For more specific instructions for contributing to pyfar packages, please check out the following:

- `Style and design guidelines <../packages/style_design.html>`_.
- `Documentation guidelines <../packages/documentation.html>`_.
- `Testing guidelines <../packages/testing.html>`_.

The documentation of each package further provides instructions including the respective commands and tools, please refer to the guide of the package you want to contribute to.
See for example the guidelines for `contributing to pyfar <https://pyfar.readthedocs.io/en/stable/contributing.html>`_

Similarly, contribution guidelines exist for the *pyfar gallery* and the *open educational resources*:

- `Contribution guidelines for the gallery <../contribution_gallery.html>`_.
- `Contribution guidelines for the open educational resources <../contribution_oer.html>`_.


Submitting a Pull Request
-------------------------

To get your changes merged into a pyfar repository or project, you need to submit a pull request (PR) on GitHub.
A general guide on PRs can be found on the `GitHub documentation <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests?platform=linux>`_.

Before Submitting a Pull Request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please make sure to meet the following criteria:

- Ensure that the PR targets the correct branch, i.e. ``main`` if you are proposing a bugfix or improvements to the documentation, or ``develop`` if you propose a new feature or enhancement of existing code.
- Pyfar projects follow `semantic versioning <../packages/releasing.html#versioning>`_. This means that
   - Changes to existing functionality are only allowed in minor or major releases (``develop`` branch) under the condition that backward compatibility is maintained for at least two minor releases.
   - If required, deprecations of existing functionality can be introduced to ensure backward compatibility.
   - Breaking changes are only allowed in major releases.
- Ensure that your code follows the `coding style and guidelines of the project <../packages/style_design.html>`_.
- Ensure to add or update tests as necessary and that all tests pass. Please refer to the `testing guidelines <../packages/testing.html>`_ for more information.
- Include a clear and concise docstring which is formatted according to the project's documentation guidelines and make sure that it is added to the API documentation.
- Keep contributions made in a PR as compact and module as possible. It is always beneficial to re-use existing functionality when suitable.
- Please refrain from making changes on code sections that are not related to the PR. This is to ensure that the git history remains clear and improves maintainability and most importantly makes reviewing a PR easier.
- Please avoid purely cosmetic formatting changes. Maintainers will usually ask you to revert unrelated or purely cosmetic changes for maintainability reasons.
- Please keep the git history as clean as possible and write descriptive and meaningful commit messages. Commit messages such as `"add fix"` are not descriptive enough.

Once all criteria are met, you can create the PR through the GitHub interface.

When Creating the Pull Request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please make sure to consider the following points when creating the PR:

- Provide a clear and descriptive title for the PR.
- Write a detailed description of the changes made in the PR, including the motivation behind them and any relevant context.
- If the PR addresses any existing issues, link them using the ``closes #issue-number`` syntax. Note that an existing issue does not mean that you can simply skip the PR description.
- Browse the available labels and assign the most appropriate ones to your PR.
- If possible, add the PR to the *Weekly meeting* project board. Workflow automation will then assign the status :backlog:`Backlog` which is automatically updated during the process.
- If a milestone is already defined for the next release you can also assign it to the PR. Otherwise, maintainers will take care of this later. Please ignore the corresponding (failing) workflow check.


The Review Process
~~~~~~~~~~~~~~~~~~

- If you open a PR which is not yet ready for review, mark it as "Draft". You can request reviews for draft PRs, but reviewers will know that it is not yet ready for final review and consequently provide conceptual feedback only. You can also indicate that you want to discuss the PR further by changing the status to :open-discussion:`Open Discussion` in the project section.
- As soon as the PR is ready for review, request a review from the maintainer team of the respective package or project. The teams are named after the respective repository. Remember to change the status from "Draft" to "Ready for Review" if applicable. Please note that it might take some time for reviewers to get to your PR depending on their availability. If you have not received feedback after a reasonable amount of time, feel free to ping the maintainers once more or get in touch through slack or join a weekly developer meeting.
- Wait for the reviewers feedback and address the requested changes if necessary. Pyfar requires at least two approving reviews before a PR can be merged. For small changes, such as fixing small issues or updating the documentation, one approving review is usually sufficient.
- You can also refer to the `reviewer guidelines <reviewing.html>`_ for more information on the review process.
- If recent changes made to the ``main`` or ``develop`` branch are required for your PR, use ``git rebase`` instead of ``git merge``. This helps maintainability of the project.
- During the review process, please only update the PR description if necessary or a reviewer requests it. To reply to reviewer comments, please use the comment functionality of GitHub instead.
- If you find that during the review process the commit history gets very long consider squashing it using an interactive rebase. If maintainers find the commit history insufficiently compact they will either ask you to condense the history or squash the entire PR into a single commit when merging.