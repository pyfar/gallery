============
Installation
============

Use pip to install any pyfar package. For example the base package *pyfar* is installed by

.. code-block:: console

    $ pip install pyfar

(Requires Python 3.8 or higher)

Reading and writing audio files is supported through `SoundFile`_, which is based on `libsndfile`_. On Windows and OS X, it will be installed automatically. On Linux, you need to install libsndfile using your distribution’s package manager, for example

.. code-block:: console

    $ sudo apt-get install libsndfile1


Best practice
=============

We recommend to install pyfar into a python environment to avoid conflicts with already installed packages. The example below uses the `Anaconda`_ package manager. To create a new environment run

.. code-block:: console

    $ conda create --name pyfar python

Now activate the environment with

.. code-block:: console

    $ conda activate pyfar

After this, you can install pyfar into the environment as shown above. For more information we recommend the `Managing environments`_ tutorial.


.. _SoundFile: https://pysoundfile.readthedocs.io/en/latest/
.. _libsndfile: http://www.mega-nerd.com/libsndfile/
.. _Anaconda: https://www.anaconda.com/
.. _Managing environments: https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
