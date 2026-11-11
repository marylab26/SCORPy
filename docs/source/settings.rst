Prepare and import data
=======================

Project directory
-----------------

In **Project Settings**, select the path to the working directory ``your_project`` organized as follows:

.. code-block:: text

   your_project/
     data/               <-- required, even if initially empty
       sample01.csv
       sample02.csv
     metadata/           <-- required, even if initially empty
       ometif.csv        <-- optional but required for exposure-aware background correction
       annotations.csv   <-- optional, but recommended for sample grouping and metadata integration

``ometif.csv`` and ``annotations.csv`` are example filenames, not a complete
metadata specification. Exposure times are needed for exposure-aware background
correction; sample annotations are optional.

SCORPy creates output directories for processing results. Their purpose is
described in :doc:`exports`.

Single-cell tables and column names
-----------------------------------

Each row should describe a segmented cell. Depending on the intended
analysis, for example working on TMA data, the table needs sample (slide) 
and Region of Interest (ROI) identifiers, marker intensities, and spatial coordinates (X, Y) usually in pixels.

Intensity columns encode a marker, localization, and measurement metric.
Recognized naming examples:

.. list-table::
   :header-rows: 1

   * - Convention
     - Example
   * - Underscore-delimited
     - ``CD3_Cell_Intensity_Average``
   * - Space-delimited
     - ``CD3 Cell Intensity Average``
   * - Colon-delimited
     - ``CD3: Cell: Mean``

Non-intensity columns such as ``Sample_ID``, ``ROI_index``, and
``Nucleus_Size`` are recognized through aliases. Check the application's
**Instruction** tab for the accepted aliases in your release. Do not assume
every export from a supported imaging platform uses compatible headers.

Import, merge, and inspect
--------------------------

1. Open **Input Files** and select the CSV files to combine.
2. Review file-validation feedback before proceeding. Checks for empty files, duplicate headers, and encoding problems.
3. Inspect the merged dataset and quality report, including missing values
   and differences in column coverage.
4. Confirm that sample and ROI identifiers distinguish the tissues you intend
   to analyze separately.

Merging tables does not establish that their measurements are comparable.
Check marker panels, units, and preprocessing history before combining data.

Exposure-time metadata
----------------------

For exposure-aware background correction, provide the exposure times of
both marker and matched autofluorescence measurements. The correction must
match the fluorophore/channel and subcellular compartment.

Use the exposure-time example associated with the manuscript or example
dataset, and check its mapping against the imported columns. An incorrect mapping can change the corrected
signal even when the file imports successfully. Exposure time are usually in milliseconds (ms).

.. csv-table:: Exposure-time.csv or ometif.csv example
   :header: ChannelIndex, Cycle, Name, ExposureTime

   0, 0, DAPI0, 3
   1, 0, AF488, 500
   2, 0, AF555, 1500
   3, 0, AF647, 1500
   4, 0, AF750, 1500
   0, 1, DAPI1, 2
   1, 1, CA9, 100
   2, 1, B7H4, 800
   3, 1, pAKT, 1200
   4, 1, CD44, 200
   ...,...,...,...


Sample annotations
------------------

Annotations can describe experimental groups, patients, treatments, or tissue
types. Join annotations using ``Sample_ID`` and
``ROI_index``.

Preview the annotation table, select the columns to include, and inspect
matched and unmatched rows after merging. Check that join-key combinations
are unique where one annotation record per sample/ROI is intended. Unexpected
duplicates or unmatched identifiers should be resolved before group comparisons.

.. csv-table:: annotation.csv example (TMA version)
   :header: Sample_ID, ROI_index, Group, PatientID, Treatment

   slide1.csv, 0, Control, Patient1, DrugA
   slide1.csv, 1, Control, Patient1, DrugA
   slide1.csv, 2, Control, Patient2, DrugB
   slide2.csv, 0, Treatment, Patient3, DrugA
   slide2.csv, 1, Treatment, Patient4, DrugB
   slide2.csv, 2, Treatment, Patient4, DrugB
   ...,...,...,...,...

.. csv-table:: annotation.csv example (whole-tissue slide version)
   :header: Sample_ID, ROI_index, Group, PatientID, Treatment

   slide1.csv, 0, Control, Patient1, DrugA
   slide2.csv, 0, Control, Patient1, DrugA
   slide3.csv, 0, Treatment, Patient3, DrugA
   slide4.csv, 0, Treatment, Patient3, DrugA     
   slide5.csv, 0, Treatment, Patient4, DrugB
   ...,...,...,...,...

**Next:** continue with :doc:`preprocessing`, or use the
:doc:`starting-point guide <installation>` for already processed data.
