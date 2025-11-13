.. pyfar gallery documentation master file, created by
   sphinx-quickstart on Fri Feb 16 11:37:48 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. |pyfar_logo| image:: resources/logos/pyfar_logos_fixed_size_pyfar.png
   :width: 150
   :alt: Alternative text

.. include:: header.rst

pyfar - python packages for acoustics research
==============================================


Pyfar aims at providing signal processing methods, plotting functionality, and
interfacing with audio devices and instrumentation in a unified and
comprehensive framework for acoustics research. To ensure  good usability, the
pyfar ecosystem is developed with a strong focus on documentation. Test driven
development and continuous integration ensure stable and reliable code. Pyfar
packages are provided under the MIT open source license allowing unrestricted
educational and commercial use.

.. admonition:: Getting started

      - If you are new to pyfar, we recommend the `Pyfar examples gallery`_, which works online.
      - If you want to install a specific package, please refer to their documentation below.
      - If you have trouble with pyfar, please refer to the `Help section`_.

|

.. grid:: 1 2 2 3
   :gutter: 4

   .. grid-item-card:: Python package for acoustics research
      :text-align: justify
      :shadow: lg

      .. image:: resources/logos/pyfar_logos_fixed_size_pyfar.png
         :width: 300 px
         :target: https://pyfar.readthedocs.io/

      ^^^


      The pyfar base package offers functionality for digital signal
      processing, signal generation, and plotting.
      +++
      .. grid:: 2

         .. grid-item::

            .. button-link:: https://pyfar.readthedocs.io/
               :color: primary
               :shadow:
               :expand:

               docs

         .. grid-item::

            .. button-link:: https://github.com/pyfar/pyfar
               :color: primary
               :shadow:
               :expand:

               code

   .. grid-item-card::  Python package for handling SOFA files
      :text-align: justify
      :shadow: lg

      .. image:: resources/logos/pyfar_logos_fixed_size_sofar.png
         :width: 300 px
         :target: https://sofar.readthedocs.io

      ^^^
      SOFA files store spatially distributed acoustic data such as head-related
      transfer functions. Sofar can read, create, write, manipulate, and verify
      SOFA files.
      +++
      .. grid:: 2

         .. grid-item::

            .. button-link:: https://sofar.readthedocs.io
               :color: primary
               :shadow:
               :expand:

               docs

         .. grid-item::

            .. button-link:: https://github.com/pyfar/sofar
               :color: primary
               :shadow:
               :expand:

               code

   .. grid-item-card::  Spherical array processing in python
      :text-align: justify
      :shadow: lg

      .. image:: resources/logos/pyfar_logos_fixed_size_spharpy.png
         :width: 300 px
         :target: https://spharpy.readthedocs.io

      ^^^
      Spherical array processing in python
      +++
      .. grid:: 2

         .. grid-item::

            .. button-link:: https://spharpy.readthedocs.io
               :color: primary
               :shadow:
               :expand:

               docs

         .. grid-item::

            .. button-link:: https://github.com/pyfar/spharpy
               :color: primary
               :expand:
               :shadow:

               code

   .. grid-item-card:: Python Room Acoustics Tools
      :text-align: justify
      :shadow: lg

      .. image:: resources/logos/pyfar_logos_fixed_size_pyrato.png
         :width: 300 px
         :target: https://pyrato.readthedocs.io

      ^^^^
      A collection of functions for commonly used operations in room acoustics.
      +++
      .. grid:: 2

         .. grid-item::

            .. button-link:: https://pyrato.readthedocs.io
               :color: primary
               :shadow:
               :expand:

               docs

         .. grid-item::

            .. button-link:: https://github.com/pyfar/pyrato
               :color: primary
               :expand:
               :shadow:

               code

   .. grid-item-card:: coming next...
      :text-align: justify
      :shadow: lg

      .. image:: resources/logos/pyfar_logos_fixed_size_coming.png
         :width: 250 px
         :target: https://github.com/pyfar

      ^^^^
      The pyfar base package will be extended. New packages for audio
      input/output to external hardware, acoustic measurements,
      and material modeling are planned.
      +++
      .. grid:: 1

         .. grid-item::

            .. button-link:: https://github.com/pyfar
               :color: primary
               :expand:
               :shadow:

               progress

|

Examples
========

This is the pyfar gallery. It provides a collection of examples and tutorials
for the whole pyfar ecosystem.

.. grid:: 1 2 2 3
   :gutter: 4

   .. grid-item-card::
      :link: examples_gallery.html#getting-started
      :text-align: center

      Getting Started
      ^^^^

      .. image:: _static/thumbnail_pyfar_audio_objects.png
         :width: 200 px

   .. grid-item-card::
      :link: examples_gallery.html#applications
      :text-align: center

      Applications
      ^^^^

      .. image:: _static/thumbnail_sofar_introduction.png
         :width: 200 px

   .. grid-item-card::
      :link: examples_gallery.html#workshops
      :text-align: center

      Workshops
      ^^^^

      .. image:: _static/pyfar_pf_transparent.png
         :width: 150 px


Open Educational Resources
==========================

We host a collection of open educational resources for teaching acoustics.
The collection primarily includes assignments in the form of Jupyter notebooks.

.. grid:: 1 2 2 3
   :gutter: 4

   .. grid-item-card::
      :link: https://pyfar-oer.readthedocs.io/en/latest/open_educational_resources.html#pyfar-assignments
      :text-align: center

      Intro to pyfar
      ^^^^

      .. image:: _static/pyfar_pf_transparent.png
         :width: 150 px

   .. grid-item-card::
      :link: https://pyfar-oer.readthedocs.io/en/latest/open_educational_resources.html#var-tub
      :text-align: center

      Virtual Acoustic Reality (TUB)
      ^^^^

      .. image:: _static/TUB_VAR_sound_field.png
         :width: 150 px


   .. grid-item-card::
      :link: https://pyfar-oer.readthedocs.io/en/latest/open_educational_resources.html#val-fau
      :text-align: center

      Virtual Acoustics Lab (FAU)
      ^^^^

      .. image:: _static/Artificial-Audio-Logo.jpg
         :width: 150 px


Supporters
==========

.. grid:: 2 4 6 6
   :gutter: 2

   .. grid-item-card::
      :link: https://www.tue.nl/en/research/research-groups/building-physics-and-services/building-acoustics
      :text-align: center
      :class-body: bg-logo-card

      .. image:: resources/supporter-logos/TUe-logo-scarlet-L.png
         :width: 250 px

   .. grid-item-card::
      :link: https://www.akustik.rwth-aachen.de/go/id/dwma/
      :text-align: center
      :class-body: bg-logo-card

      .. image:: resources/supporter-logos/ITHA_RWTH_fixed_size.png
         :width: 250 px

   .. grid-item-card::
      :link: https://www.tu.berlin/ak/
      :text-align: center
      :class-body: bg-logo-card

      .. image:: resources/supporter-logos/TU_AK_fixed_size.png
         :width: 250 px

   .. grid-item-card::
      :link: https://www.th-koeln.de/informations-medien-und-elektrotechnik/technische-akustik_25051.php
      :text-align: center
      :class-body: bg-logo-card

      .. image:: resources/supporter-logos/TH_Koeln_fixed_size.png
         :width: 250 px

   .. grid-item-card::
      :link: https://www.tu.berlin/akustik
      :text-align: center
      :class-body: bg-logo-card

      .. image:: resources/supporter-logos/tu-berlin-logo-long-red_fixed_size.png
         :width: 250 px

   .. grid-item-card::
      :link: https://electro.dtu.dk/research/research-areas/electro-technology/acoustic-technology
      :text-align: center
      :class-body: bg-logo-card

      .. image:: resources/supporter-logos/DTU_fixed_size.png
         :width: 250 px

   .. grid-item-card::
      :link: https://www.lms.tf.fau.eu/person/prof-dr-ing-sebastian-schlecht/
      :text-align: center
      :class-body: bg-logo-card

      .. image:: resources/supporter-logos/FAU_LMS_fixed_size.png
         :width: 250 px
         :align: center

   .. grid-item-card::
      :link: https://www.aalto.fi/en/aalto-acoustics-lab
      :text-align: center
      :class-body: bg-logo-card

      .. image:: resources/supporter-logos/aalto_fixed_size.png
         :width: 250 px
         :align: center

   .. grid-item-card::
      :link: https://www.southampton.ac.uk/about/faculties-schools-departments/school-of-engineering/institute-of-sound-and-vibration-research
      :text-align: center
      :class-body: bg-logo-card

      .. image:: resources/supporter-logos/university_southhampton_fixed_size.png
         :width: 250 px
         :align: center

   .. grid-item-card::
      :link: https://www.int.uni-rostock.de/Signalverarbeitung-und-virtuel.spva+B6Jkw9MA__.0.html
      :text-align: center
      :class-body: bg-logo-card

      .. image:: resources/supporter-logos/Uni_Rostock_fixed_size.png
         :width: 250 px
         :align: center

   .. grid-item-card::
      :text-align: center
      :class-body: bg-logo-card

      .. image:: resources/supporter-logos/iap_fixed_size.png
         :width: 250 px


.. _Pyfar examples gallery: examples_gallery.rst
.. _Help section: help/index.rst
