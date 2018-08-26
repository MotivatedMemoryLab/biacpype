=========
biacpype
=========
.. image:: https://travis-ci.org/MotivatedMemoryLab/biacpype.svg?branch=master
    :target: https://travis-ci.org/MotivatedMemoryLab/biacpype    
.. image:: https://coveralls.io/repos/github/MotivatedMemoryLab/biacpype/badge.svg
    :target: https://coveralls.io/github/MotivatedMemoryLab/biacpype


This repo serves as a pipeline for analyzing data from Duke Brain Imaging & 
Analysis Center `(biac) <https://www.biac.duke.edu>`_ supporting data format conversion 
(to `BIDS <http://bids.neuroimaging.io/>`_) and common data analysis with `FSL <https://fsl.fmrib.ox.ac.uk/fsl/fslwiki>`_

-------------
Documentation
-------------
Please check out `<https://motivatedmemorylab.github.io/biacpype>`_ for code documentation.
You can also find a user manual `here`_.

.. _here: https://motivatedmemorylab.github.io/biacpype/manual/manual.pdf


------------
Installation
------------
To install the package, clone this repo, then run the following:

.. code-block:: python

    python setup.py install

We intent to only support Python3. 

-------
Modules
-------
1. :code:`biac2bids`: conversion from BIAC format (:code:`.nii.gz` & :code:`.bxh`) to BIDS



