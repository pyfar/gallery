DEP-0: Definition of the pyspar package
=======================================

| **Author(s):** Marco Berzborn, Fabian Brinkmann, George Papadimitriou
| **Status:** Draft
| **Type**: Package Definition
| **Created:** 06.11.2026


Demand
------

- Existing (high number of downloads for SDM package for MATLAB).
- Array based binaural rendering is a relevant topic in audio for VR/AR/MR.

Scope
-----

- Implement and provide parametric spatial audio methods in a consistent framework

  - Methods for SRIRs (first)
  - Methods for Streams (later)

- Parameter estimation

  - direction of arrival (DoA)
  - diffuseness
  - number of sources

- Plots for estimated parameters

Overlap with and separation from other (existing) packages
------------------------------------------------------------

This section should ensure that the proposed package does not create overlap with already existing packages.
The intention is to define a package with separate scope and functionality.
Overlap means that functionality can be implemented in other packages and finally imported into proposed package.

- Strong overlap with spharpy
- Overlap with pynaural (nonexistent)
- Use: pyfar.Signals, pyfar.Coordinates, spharpy.SHSignals
- Microphone array class could be implemented in spharpy

Alternatives
------------

- Could this idea be realised in another package? *— skipped*

Team
----

- Including the roles if already defined (e.g. maintainer, developer, etc.)

- Nils
- George
- Fabian
- Marco
- Anton

Copyright
----------

This document has been placed in the public domain.
