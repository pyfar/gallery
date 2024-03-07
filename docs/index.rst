.. pyfar gallery documentation master file, created by
   sphinx-quickstart on Fri Feb 16 11:37:48 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


.. |pyfar_logo| image:: resources/pyfar_logos_fixed_size_pyfar.png
   :width: 150
   :alt: Alternative text

pyfar - python packages for acoustics research
==============================================


Pyfar aims at providing signal processing methods, plotting functionality, and 
interfacing with audio devices and instrumentation in a unified and 
comprehensive framework for acoustics research. To ensure  good usability, the 
pyfar ecosystem is developed with a strong focus on documentation. Test driven 
development and continuous integration ensure stable and reliable code. Pyfar 
packages are provided under the MIT open source license allowing unrestricted 
educational and commercial use.

|

.. grid:: 3
   :gutter: 4

   .. grid-item-card:: python package for acoustics research
      :text-align: center
      :shadow: lg

      .. image:: resources/pyfar_logos_fixed_size_pyfar.png
         :width: 300 px
      
      ^^^
      

      The pyfar base package offers functionality for digital signal 
      processing, signal generation, and plotting.
      +++
      .. grid:: 2
         
         .. grid-item::

            .. button-link:: https://pyfar.readthedocs.io/en/stable/ 
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

   .. grid-item-card::  maybe the most complete python package for SOFA files so far
      :text-align: center
      :shadow: lg

      .. image:: resources/pyfar_logos_fixed_size_sofar.png
         :width: 300 px

      ^^^
      SOFA files store spatially distributed acoustic data such as head-related 
      transfer functions. Sofar can read, create, write, manipulate, and verify 
      SOFA files.
      +++
      .. grid:: 2
      
         .. grid-item::

            .. button-link:: https://sofar.readthedocs.io/en/stable/ 
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
      :text-align: center
      :shadow: lg
   
      .. image:: resources/pyfar_logos_fixed_size_spharpy.png
         :width: 300 px

      ^^^
      Spherical array processing in python
      +++
      .. grid:: 2

         .. grid-item::

            .. button-link:: https://spharpy.readthedocs.io/en/latest/ 
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
      :text-align: center
      :shadow: lg

      .. image:: resources/pyfar_logos_fixed_size_pyrato.png
         :width: 300 px

      ^^^^
      A collection of functions for commonly used operations in room acoustics
      +++
      .. grid:: 2
      
         .. grid-item::

            .. button-link:: https://pyrato.readthedocs.io/en/latest/ 
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

   .. grid-item-card::  
      :text-align: center
      :shadow: lg

      **coming next...**
      ^^^^
      The pyfar base package will be extendend an new packages for audio 
      input/output to external hardware, acoustic measurements, 
      and spherical array processing are planned.
      +++
      .. grid:: 1

         .. grid-item::

            .. button-link:: https://github.com/pyfar
               :color: primary
               :expand:
               :shadow:
 
               progress 


|
Pyfar gallery
=============

This is the pyfar gallery. It provides a collection of examples and tutorials
for the whole pyfar ecosystem.



.. nbgallery::
   :caption: Getting Started
   :name: pyfar_gallery
   :glob:
   :reversed:

   gallery/interactive/pyfar_audio_objects.ipynb
   gallery/interactive/sofar_introduction.ipynb
   gallery/interactive/pyfar_filter_types.ipynb
   gallery/interactive/pyfar_arithmetics.ipynb
   gallery/interactive/pyfar_filtering.ipynb

.. nbgallery::
   :caption: Acoustic measurements
   :name: measurement
   :glob:
   :reversed:

   gallery/static/impulse_response_measurement.ipynb




|
Contribute  
===========

Pyfar is completely open source and it’s license allows unrestricted 
educational and commercial use. It is made by the acoustics research 
community for the acoustics research community. We welcome any contributions
– go ahead if you are in the mood.

.. grid:: 2
   

   .. grid-item-card::
      :text-align: center

      **Feedback, bugs, feature requests**
      ^^^^
      The best way for any feedback, bug reports, and feature request is to 
      open a new issue on GitHub. The GitHub projects are linked through the 
      Code buttons above.

   .. grid-item-card::
      :text-align: center

      **Add code, documentation, or funding**
      ^^^^

      If you want to add code or documentation, a good starting point for ideas
      are the issues on GitHub. The GitHub projects are linked through the 
      Code buttons above. If you have own ideas for contributions, may it be 
      code, or other things, it would be best to get in touch through GitHub 
      or info@pyfar.org before you start.

|
Supporters
===========

.. grid:: 2
   :gutter: 2

   .. grid-item::
      :columns: 8

      .. grid:: 2
         :gutter: 4

         .. grid-item-card:: 
            :link: https://www.akustik.rwth-aachen.de/go/id/dwma/
            :text-align: center

            .. image:: resources/supporter-logos/ITHA_RWTH.svg
               :width: 250 px


            Institute for Hearing Technology and Acoustics, RWTH Aachen University

         .. grid-item-card:: 
            :link: https://www.tu.berlin/ak/
            :text-align: center

            .. image:: resources/supporter-logos/TU_AK.png
               :width: 250 px

            Audio Communication Group, Technical University of Berlin

         .. grid-item-card:: 
            :link: https://www.th-koeln.de
            :text-align: center

            .. image:: resources/supporter-logos/TH_Koeln.png
               :width: 250 px

            University of Applied Sciences Cologne

         .. grid-item-card:: 
            :text-align: center

            .. image:: resources/supporter-logos/iap.png
               :width: 250 px

            The Institute for Advanced Procrastination

   .. grid-item::
      :columns: 4

      .. grid:: 1
         
         .. grid-item-card:: 
            :link: https://www.dtu.dk/english/
            :text-align: center

            .. image:: resources/supporter-logos/DTU.png

            Technical University of Denmark