================
Trouble shooting
================

The installation fails
======================

Pyfar packages do not always work with the latest Python version. If the installation fails, try to restrict the Python version inside your environment, for example with

.. code-block:: console

    $ conda create --name pyfar python'<3.12'


Writing/reading audio files does not work
=========================================

Reading and writing audio files is supported through `SoundFile`_, which is based on `libsndfile`_. On Linux, you need to install libsndfile using your distribution’s package manager, for example

.. code-block:: console

    $ sudo apt-get install libsndfile1


A pyfar package is installed but can not be imported
====================================================

Make sure that you have selected the correct virtual Python environment in which you installed pyfar. If you are using conda, you can activate an environment by

.. code-block:: console

    $ conda activate pyfar

in which 'pyfar' is the name of the environment. For more information on conda, we recommend the `Managing environments`_ tutorial.

.. _SoundFile: https://pysoundfile.readthedocs.io/en/latest/
.. _libsndfile: http://www.mega-nerd.com/libsndfile/
.. _Managing environments: https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
