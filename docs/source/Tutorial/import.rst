Configure the project and import data
=====================================

**Input:** the directory prepared in :doc:`tma`.

Select the working directory
----------------------------

1. Launch SCORPy and open **Project Settings**.
2. Select ``ctTMA_project`` as the working directory.
3. Check that the expected output directories are created.

.. admonition:: Screenshot to add

   Capture Project Settings with the selected project and output directories.
   Hide personal parts of the filesystem path.

Import the raw table
--------------------------------

1. Open **Input Files** and select ``data/ctTMA_raw.csv``.
2. Review validation feedback and inspect the imported table.
3. Check marker columns, spatial coordinates, and sample/ROI identifiers.

Do not include ``ctTMA_classified.csv`` in this import. Record the imported
row count and number of distinct sample/ROI combinations for comparison
after filtering.

Attach metadata
---------------

1. Load ``metadata/ctTMA.ome.tif.csv`` as exposure metadata and inspect how
   its entries map to marker and autofluorescence measurements.
2. Load ``metadata/ctTMA_annotations.csv`` as annotations.
3. Review the sample and ROI join keys and choose the annotation columns.
4. Inspect matched and unmatched rows before proceeding.

.. admonition:: Screenshot to add

   Capture the imported-table preview, exposure mapping, and annotation merge
   report. Show the tissue labels and identifiers needed to understand the join.

Check before continuing
-----------------------

Confirm that the expected marker measurements and tissue annotations are
available, and resolve unexpected unmatched identifiers. Save the import
summary with your analysis records.

**Next:** :doc:`preprocessing`. For input conventions, see :doc:`../settings`.
