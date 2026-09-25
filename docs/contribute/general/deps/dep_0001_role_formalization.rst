DEP-1: Formalization of Roles
=============================

| **Author(s):** Marco Berzborn, Hanna Chmeruk
| **Status:** Draft
| **Type**: Process
| **Created:** 25.09.2026


Roles and Responsibilities
---------------------------

Structure description
~~~~~~~~~~~~~~~~~~~~~~

The current and future structure of the pyfar project was discussed at the retreat.
The project should not have a BDFL (Benevolent Dictator for Life) who makes decisions alone or takes responsibility for the entire project.
The opinions and suggestions of all project members should be respected and may form the basis for the final decision.

The project organization should now include the Steering Committee,
i.e. a group of people who are required to be involved in important organizational, technical, and process/meta level decisions and who are responsible for the overall direction of the project.

Each individual should have clear roles and responsibilities; the roles can be categorised as follows:

- Contributor,
- Developer,
- Maintainer,
- Reviewer,
- Triage,
- Community Manager.

With the exception of the Community Manager, each role is assigned to individuals within a single package.
There should be only one Community Manager, who is in charge of the entire pyfar project.

The minimum number of people in each role depends on the size of the package and its workload.
Package maintainers should ensure that there are enough people in each role.
For maintainer roles, this responsibility lies with the steering council.
For all roles, people who have been inactive for a certain period should be contacted and removed from their role if they do not respond.

.. note:: Marco

  This needs to be updated with new roles

.. image:: https://hackmd.io/_uploads/SknbiVt-fx.png
  :alt: Roles model of the pyfar project

Steering Council
~~~~~~~~~~~~~~~~

The responsibilities of the steering council are found in the governance section of the contribution guidelines.


Community Manager
~~~~~~~~~~~~~~~~~

A Community Manager is responsible for communicating with the pyfar community by posting general announcements on communication channels, organizing and/or coordinating events (e.g. retreats, workshops), and ensuring that the project remains welcoming and friendly to newcomers.

Package specific roles
~~~~~~~~~~~~~~~~~~~~~~

Contributor
^^^^^^^^^^^

A Contributor is anyone who contributes to a package in any way. So, if someone has simply submitted reviews, added an issue or created a pull request, that person is considered a Contributor.
This is not a category that needs to be assigned, every contributor can be listed.
Contributors are not necessarily part of the pyfar organization.


Developer
~~~~~~~~~

* Someone who contributed (extensively) to pyfar in the past and wants to take up more responsibility.
* Role should be encourage feeling of responsibility for the package in question.
* Self nomination as well as on initiative by maintainers can be possible, final decisions will be up to the maintainers (welcoming culture is encouraged however).
* Developers in general should be named in the respective section and be part of the pyfar organization on GitHub.

**Required experience level:**
Basic, some experience with pyfar recommended but not required. Newcomers encouraged.


Reviewer
^^^^^^^^

A Reviewer is responsible for reviewing pull requests in the corresponding package.
A Reviewer does not necessarily need to be an experienced developer for the package themselves,
as long as they have a sufficient understanding of the suggested code and can provide constructive feedback.
Different types of reviews can be provided catering different aspects of a pull requests and levels of detail.

A more detailed description of the review process will be developed and added to the contribution guidelines in the future.


**Required experience level:**
Reviewers can work on different experience levels. Basic experience suffices for basic review (encouraged for newcomers as well), for detailed technical reviews some experience is recommended.

Triage
^^^^^^

A Triage (aka Issue Manager) should take care of managing issues and pull requests in the specific package. The concrete tasks of a Triager are:

- General:

  - Close PRs and issues if they have already been fully implemented or if it has been decided to close them (e.g. during a discussion in the weekly meeting).
  - Check the labels, milestone, name of the PR/issue, assignees, status on issues and pul requests, development status and relationships to other PRs/issues.
  - If this has not already been done by the author of the PR/issue, estimate the size and priority and add to the project board.
  - If a PR or an issue has not been updated or seen attention for a certain period of time (e.g. one month for PRs and three months for issues), notify the Maintainer and discuss the reasons for this.

- For a PR:

  - Request the right reviewers to review the PR.
  - Check if existing issues are correctly referenced.

- For an issue:

  - Check whether it was created in the correct package.
  - Check whether it is correctly categorized.
  - Check if the report is complete enough to reproduce the issue.
  - Mark potential duplicates and/or related issues.
  - Label it as 'good first issue' if it is appropriate for newcomers.

**Required experience level:**
None, encouraged for newcomers


Maintainer
^^^^^^^^^^

The responsibilities of a Maintainer include:

- Representing the package in the steering council and meetings.
- Establishing the technical direction.
- Acquiring/accepting new developers, triagers, and reviewers for the package.
- Ensuring that the infrastructure of the package is up to date, such that developers can work efficiently and effectively.
- Merging pull requests after all reviews have been completed. Maintainers are responsible for the final decision if sufficient reviews have been provided and the PR can be merged.
- Coordinating releases.

**Required experience level:**

At least 1-2 years of active experience in developing the respective package.
Maintainers will be appointed by the steering council, but self-nominations are also possible. The final decision will be made by the steering council.

.. note:: Marco

   The review related part should be moved to the respective section in the contribution guidelines.

Maintainers are responsible for
Before merging a pull request, a Maintainer should should check the following items:

- Did all CircleCi tests pass?
- Were all types of review provided? (See the section Review for more details.)
- In which branch should this PR be merged? Is the correct one selected?
- When is the right time to merge this PR? Is it connected to any releases?


Open Discussion Roles
~~~~~~~~~~~~~~~~~~~~~

List of questions regarding roles and the organisational structure to be discussed:

Maintainer
^^^^^^^^^^

.. note:: Hanna

  Requierements to be a Maintainer: similar to the rules for the Committee members

.. note:: Meeting

  Similar to the steering council: 1-2 years in the development

.. note:: Hanna

  What is the maximum and the minimum number of Maintainers a package should have?

.. note:: Meeting

  Maximum depending on the package size, minimum 1 person.

.. note:: Hanna

  Should a Maintainer also have the authority to close issues and PRs without discussing it with the rest of the team?

.. note:: Meeting

  Depending on the situation, but the Maintainer(s) should always write a reason(s) for closing an issue/PR.

.. note:: Hanna

  How many packages is one Maintainer allowed to maintain at the same time? (Should be discussed to avoid overloading one single person and to prevent the establishment of a BDFL.)

.. note:: Meeting

  No strict limitation, the Committee can discuss this.

.. note:: Hanna

  Should only the Maintainers be able to add or remove items from the Agenda on the project board?

.. note:: Meeting

  No, everyone can add items, remove only things you put on the agenda by yourself.

Contributor
^^^^^^^^^^^

.. note:: Hanna

  Is every other role a subset of the Contributor role? So, if someone is a Reviewer, Maintainer, Triage or Community Manager, are they automatically considered a Contributor?

.. note:: Meeting

  No, Contributor is a separate role, not a "parent class".

Reviewer
^^^^^^^^

.. note:: Hanna

  It is still to be discussed whether the role of Reviewer should also be divided into the roles of Technical Reviewer, Test Reviewer and Documentation Reviewer, or whether the role of Reviewer should be kept general and the distinction between the different types of Reviewer should be made via checkboxes in the pull requests themselves.

.. note:: Marco Berzborn

  During the retreat, the favored option was to not further subdivide the role, but have a list of items that are checked when they were considered in the review. Items which were not considered during the review are left open. The maintainer finally decides if the reviews are sufficient and if the PR can be merged.

Triage
^^^^^^

.. note:: Hanna

  Should all Triages also be responsible for cleaning up the project board and sorting the issues and PRs on it? Or is that rather a task for the Maintainers?

.. note:: Meeting

  Sorting wrong sorted issues/PRs, extending the labels/etc. can do Triages.

.. note:: Hanna

  Should there be a rule that the Triage should open a discussion about an issue or a PR if there have been no updates for some time? In other words: should there be a deadline after which the status of the PR or issue should be reconsidered if no changes have been implemented by then?

.. note:: Meeting

  If assigned - talk to the author, if not - can just stay in the "ready for pickup".

.. note:: Hanna

  If we want to implement the rule mentioned above, we need to define the period after which the status of an issue or a PR should be reviewed.

.. note:: Marco Berzborn

  2-4 weeks seems like a feasible time period for this.



Copyright
----------

This document has been placed in the public domain.
