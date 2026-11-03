Introduction
============

What is SCORPy?
---------------

SCORPy provides an interactive workflow for multiplexed imaging spatial
single-cell proteomics. It combines data import, quality control, signal
normalization, rule-based cell phenotyping, and quantitative and spatial
analysis in a desktop application.

It is intended for researchers working with single-cell tables extracted
from segmented tissue images, without requiring programming.

Workflow and modules
--------------------

.. figure:: ../../resources/Graphical_abstract_SCORPy_overview.PNG
   :alt: CycIF data generation followed by SCORPy's four analysis modules
   :width: 100%
   :align: center

   From multiplexed imaging and single-cell data extraction to SCORPy's
   Settings, Preprocessing, Classification, and Analysis modules. A. CycIF typical experimental workflow. B. SCORPy workflow.

The interface groups the workflow into four modules:

.. list-table::
   :header-rows: 1
   :widths: 20 35 45

   * - Module
     - Tabs
     - Purpose
   * - Settings
     - Instruction, Project Settings, Input Files
     - Configure a project and integrate data and metadata.
   * - Preprocessing
     - Cleaning, Normalization
     - Inspect, filter, background-correct, and normalize intensities.
   * - Classification
     - Thresholds, Cell Classification
     - Define marker positivity and a hierarchical phenotype library.
   * - Analysis
     - Marker Analysis, Quantification, Grid Analysis, Neighborhood Analysis
     - Summarize composition, expression, and tissue organization.

The documentation separates quantitative analysis from spatial analysis
while retaining the application's module and tab names.

Scope and supported platforms
-----------------------------

SCORPy operates on data **after image registration and cell segmentation**.
It does not replace those upstream image-processing steps. Digital tissue
reconstructions display cell measurements at their coordinates; they are not
the original fluorescence images.

The platform provides Windows and macOS executables and compatibility with
CycIF, PhenoCycler (formerly CODEX), and Lunaphore COMET datasets. Compatibility
depends on the exported table structure, not only the imaging platform name.
See :doc:`settings` before importing a new export format.
