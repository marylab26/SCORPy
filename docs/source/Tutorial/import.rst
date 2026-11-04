Configure the project and import data
=====================================

**Input:** the directory prepared in :doc:`tma`.

Select the working directory
----------------------------

1. Launch SCORPy and open **Project Settings**.
2. Select ``ctTMA_project`` as the working directory.
3. Check that the expected output directories are created.

.. admonition:: Make sure `data` and `metadata` directories are present, even if empty.

   If you ever modify the content of these directories, press again `Validate structure` to apply the changes. 
   You will have to repeat some steps of your analysis if you modified the content of these directories.


.. video:: ../../../resources/ctTMA_Projet_settings.mp4
   :width: 100%
   :align: center



Import the raw table
--------------------------------

1. Open **Input Files** and select ``data/ctTMA.csv`` (raw file).
2. Review validation feedback and inspect the imported table.
3. Check marker columns, spatial coordinates, and sample/ROI identifiers.



Attach metadata
---------------

1. Load ``metadata/ctTMA.ome.tif.csv`` as exposure metadata and inspect how
   its entries map to marker and autofluorescence measurements.
2. Load ``metadata/ctTMA_annotations.csv`` as annotations.
3. Review the sample and ROI join keys and choose the annotation columns.
4. Inspect matched and unmatched rows before proceeding.

.. csv-table:: ctTMA annotations file
   :file: ../_static/ctTMA_annotations.csv
   :header-rows: 1
   :widths: auto

.. admonition:: Note

   Make sure the `Sample_ID` and `ROI_index` columns name and content correctly match the your raw data. 
   Otherwise, the join between the raw data and annotations will fail.
   If you work with whole tissue slides (or one ROI per slide), the `ROI_index` column is still required 
   but you can fill this column with a default value, such as `0` or `1`.


.. csv-table:: ctTMA exposure time file
   :file: ../_static/ctTMA.ome.tif.csv
   :header-rows: 1
   :widths: auto

.. admonition:: Note

   Only the `ChannelIndex`, `ExposureTime`, `Cycle` and `Name` columns are required in the exposure metadata file.


.. video:: ../../../resources/ctTMA_Input_files.mp4
   :width: 100%
   :align: center


**Next:** :doc:`preprocessing`. For input conventions, see :doc:`../settings`.
