DEP-0: Purpose and Process
==========================

| **Author(s):** Marco Berzborn, Hanna Chmeruk
| **Status:** Draft
| **Type**: Process
| **Created:** 10.07.2026

What is a DEP?
---------------

DEP stands for Documented Enhancement Proposal. A DEP is a design document providing information to the pyfar community, or describing a new feature for pyfar or its processes or environment. The DEP should provide a concise technical specification of the feature and a rationale for the feature.

DEPs are intended to be the primary mechanism for proposing major new features, collecting community input on an issue, and documenting design decisions that have gone into the pyfar ecosystem and it's packages.

Types
^^^^^

There are four kinds of DEPs:

1. A **Standards Track** DEP describes a new feature or implementation for a pyfar package. Examples of such DEPs are:

   - A planned feature or addition has project wide or cross-package implications.
   - A planned feature is extensive and requires substantial development effort.
   - A planned feature has broad implications for the user-facing API.

2. A **New Package** DEP describes a proposal for new packages and their integration into the pyfar ecosystem.
3. An **Informational** DEP describes a pyfar design issue, or provides general guidelines or information to the community, but does not propose a new feature. Informational DEPs do not necessarily represent a community consensus or recommendation but are intended to document reasoning and shortcomings of existing implementations.
4. A **Process/Meta** DEP describes a process surrounding pyfar, or proposes a change to a process. Process DEPs require community consensus.

DEP Workflow
-------------

The DEP process begins with a new idea for pyfar. A single DEP should contain a single key proposal or new idea. Small enhancements or patches often don't need a DEP and can be submitted directly via a pull request to the respective repository.

Each DEP must have at least one champion — someone who writes the DEP, shepherds discussions, and attempts to build community consensus around the idea.

It is recommended that at least one package maintainer is involved or consulted in the writing process, to ensure that the proposal has a clear direction which matches the scope of the pyfar ecosystem.

Standards Track DEPs consist of two parts, a design document and a reference implementation. It is generally recommended that at least a prototype implementation be co-developed with the DEP, as ideas that sound good in principle sometimes turn out to be impractical when subjected to the test of implementation. Often it makes sense for the prototype implementation to be made available as a PR to the corresponding repo (making sure to appropriately mark the PR as a draft and indicating the corresponding DEP).

DEPs should be submitted to the pyfar gallery repository, in the ``docs/contribute/general/deps`` folder. The DEP should be named ``dep-<number>-<short-title>.rst``, where ``<number>`` is a unique number assigned to the DEP and ``<short-title>`` is a short descriptive title of the proposal.

Review and Resolution
^^^^^^^^^^^^^^^^^^^^^^

The possible statuses of a DEP are:

- ``Draft`` - initial state for all DEPs
- ``Accepted`` - consensus reached in a council meeting
- ``Final`` - reference implementation completed and merged
- ``Provisional`` - accepted for inclusion but awaiting further feedback
- ``Deferred`` - no progress being made
- ``Rejected`` - not accepted after discussion
- ``Withdrawn`` - retracted by the author
- ``Superseded`` - replaced by a newer DEP
- ``Active`` - ongoing Process DEPs

All DEPs start as ``Draft``. After discussion, consensus may be reached to accept the DEP – see the next section for details – and the status becomes ``Accepted``.

Once ``Accepted``, the reference implementation must be completed and merged into the corresponding pyfar package repository before the status changes to ``Final``.

A DEP may instead be marked ``Provisional`` if it is accepted for inclusion but needs further user feedback before it can be considered ``Final``. Unlike ``Final`` DEPs, ``Provisional`` DEPs may still be ``Rejected`` or ``Withdrawn`` even after being released. Where possible, prefer reducing a proposal's scope (e.g. by deferring parts to later DEPs) over relying on ``Provisional`` status, since it can cause version compatibility issues across the pyfar ecosystem.

A DEP is ``Deferred`` by its author or a package maintainer when no progress is being made. It is ``Rejected`` if consensus decides against it, or ``Withdrawn`` if the author retracts it. In both cases the DEP is kept as a record and updated with a Resolution header linking to the relevant pull request.

A DEP can be ``Superseded`` by another, using the Replaced-By and Replaces headers (e.g. ``:ref:`DEP#number```) to cross-reference them.

Process DEPs may instead have status ``Active`` if they are never meant to be completed, e.g. DEP 0 (this DEP).

How a DEP Becomes Accepted
^^^^^^^^^^^^^^^^^^^^^^^^^^^

A DEP is ``Accepted`` by consensus of all interested contributors, with mandatory involvement from the steering council. The steering council is expected to contribute broad experience, maintain an overview of the entire ecosystem, and ensure that DEPs align with the project's overall scope and direction. The steering council further acts as a tie breaker.
To communicate the DEP with the community, send a message to the community Slack channel with a subject like:

Proposal to contribute to/discuss **DEP # <number>: <title>**

The message should:

- Link to the latest version of the DEP
- Briefly describe any major points of discussion and how they were resolved
- The state of the DEP

Feedback on a DEP can be given using GitHub pull request comments or review system. Please refrain from using the "request changes", as the responsibility of the DEP champion is to incorporate feedback and update the DEP accordingly. Final acceptance of the DEP is determined in the steering council meeting.

Maintenance
^^^^^^^^^^^

DEPs are generally not modified after reaching ``Final`` state. ``Process`` DEPs may be updated over time to reflect changes in practices. In such cases, the DEP should include a **modified date** in the header, as well as indication of what has changed. An update to a process DEP should be decided by the same process as the original DEP.

Format and Template
---------------------

DEPs are Markdown/RST files stored in the pyfar documentation repository. Each DEP must begin with the following header preamble::

    Author: <author name(s)>
    Status: <Draft | Active | Accepted | Deferred | Rejected | Withdrawn | Final | Superseded>
    Type: <Standards Track | New Package | Informational | Process>
    Created: <date>
    Requires: (optional)
    Pyfar-Package(s) and Version(s) : (optional)
    Replaces: (optional)
    Replaced-By: (optional)
    Resolution: (optional)

A template will be created which contains more information on mandatory contents of a DEP.

References
-----------

- Created by adapting `NumPy Enhancement Proposals (NEP-0) <https://numpy.org/neps/nep-0000.html>`_

Copyright
----------

This document has been placed in the public domain.
