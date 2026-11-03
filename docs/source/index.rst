SCORPy Documentation
====================

.. toctree::
   :maxdepth: 4

   installation
   Tutorial/index
   
SCORPy
======

SCORPy is a standalone, code-free desktop application for end-to-end analysis
of multiplexed imaging spatial single-cell proteomics data. It guides users
from post-segmentation CSV files through preprocessing, cell classification,
and spatial analysis.

Getting started
---------------

1. Download the latest Windows or macOS application from the
   `SCORPy releases page <https://github.com/marylab26/SCORPy/releases>`_.
2. Create a project folder containing ``data/`` and ``metadata/``
   subfolders. These folders can be empty when you first open the application.
3. Launch SCORPy and follow the **Instruction** and **Project Settings** tabs
   to configure the project and import your files.

The application creates output folders for the processing steps when you set
the project path. No Python installation is needed to use the pre-built app.

Workflow
--------

SCORPy organizes analysis into four modules:

* **Settings** — configure a project and import data, metadata, and
  annotations.
* **Preprocessing** — clean data and normalize marker intensities.
* **Classification** — set marker thresholds and classify cells.
* **Analysis** — explore markers and quantify cellular proportions, tissue
  area, density, grids, and neighborhoods.


More information
----------------

The repository `README <https://github.com/marylab26/SCORPy#readme>`_ includes
more detail on data requirements and supported formats. For help or to report
an issue, visit the
`SCORPy GitHub repository <https://github.com/marylab26/SCORPy>`_.
