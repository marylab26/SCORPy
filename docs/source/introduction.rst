Introduction
============

What is SCORPy?
---------------

SCORPy (Single-Cell proteOmics Research Platform) provides an interactive workflow for multiplexed imaging spatial
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

  SCORPy end-to-end workflow.

**(A) CycIF workflow overview.**
Tissue sections from TMAs or whole-slide samples are subjected to iterative staining cycles using a designed antibody panel, 
including an initial empty round to assess autofluorescence in each channel, followed by sequential image acquisition. 
Images are then processed through registration, artefact identification and exclusion, cell segmentation, and extraction of single-cell 
measurements to generate raw tabular datasets containing protein marker intensities, spatial coordinates, morphometric features, and sample metadata. Single-cell datasets are subsequently imported into SCORPy for data harmonization, preprocessing, quality control, and downstream single-cell and spatial analyses.

**(B) SCORPy analytical workflow.**
Input data, including raw, normalized, or pre-classified single-cell tables and associated metadata, 
are organized within a standardized project structure. SCORPy accepts single-cell data tables exported from diverse image analysis segmentation 
platforms in comma- or semicolon-separated formats. The pipeline comprises quality control, data cleaning and localization assessment, and 
normalization. Cells are classified using user-defined marker thresholds based on a mutually exclusive gating strategy, 
followed by hierarchical phenotyping. Downstream analyses include marker expression profiling, 
spatial mapping, cell-type quantification, grid-based spatial analysis, and neighborhood characterization. 
Publication-ready figures can be generated and exported along analysis parameters. 


The interface groups the workflow into four modules:

.. list-table::
   :header-rows: 1
   :widths: 20 35 45

   * - Module
     - Tabs
     - Purpose
   * - Settings
     - Instructions 📍, Project Settings ⚙️, Input Files 📂
     - Configure a project and integrate data and metadata.
   * - Preprocessing
     - Cleaning 🧹, Normalization 🚧
     - Inspect, filter, background-correct, and normalize intensities.
   * - Classification
     - Thresholds ✂️, Cell Classification 🎨
     - Define marker positivity and a hierarchical phenotype library.
   * - Analysis
     - Marker Analysis 🔎, Quantification 📊, Grid Analysis 🧊, Neighborhood Analysis 🕸️
     - Summarize composition, expression, and tissue organization.

Scope and supported platforms
-----------------------------

.. admonition:: Note

   SCORPy operates on data **after image registration and cell segmentation**.
   It does not replace those upstream image-processing steps. Digital tissue
   reconstructions display cell measurements at their coordinates; they are not
   the original fluorescence images.

The platform provides Windows and macOS executables and compatibility with
CycIF, PhenoCycler (formerly CODEX), and Lunaphore COMET datasets. Compatibility
depends on the exported table structure.

See :doc:`settings` before importing a new export format.
