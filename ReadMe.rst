=========
biacpype
=========
.. image:: https://travis-ci.org/MotivatedMemoryLab/biac2bids.svg?branch=master
    :target: https://travis-ci.org/MotivatedMemoryLab/biac2bids
    
This repo serves as a pipeline for analyzing data from Duke Brain Imaging & 
Analysis Center `(biac) <https://www.biac.duke.edu>`_ supporting data format conversion 
(to `BIDS <http://bids.neuroimaging.io/>`_) and common data analysis with `FSL <https://fsl.fmrib.ox.ac.uk/fsl/fslwiki>`_

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
    - :code:`generate_json`: generate json files needed by :code:`bxh2bids` automatically
    - :code:`bxh2bids`: conversion algorithm. Credit: `jlgraner <https://github.com/jlgraner>`_ 




