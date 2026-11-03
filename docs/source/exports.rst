Export and reproduce an analysis
================================

Tables and output directories
-----------------------------

Export results at the relevant processing and analysis stages.

.. list-table::
   :header-rows: 1

   * - Directory
     - Contents
   * - ``init/``
     - Imported and merged data
   * - ``cleaning/``
     - Cleaned data
   * - ``normalization/``
     - Normalized data
   * - ``classification/``
     - Classified data
   * - ``quantification/``
     - Quantitative exports and derived variables
   * - ``figures/``
     - Exported visualizations


Figures and tissue reconstructions
----------------------------------

Use the available figure export controls and inspect the saved file.
Retain plotted data with the figure where possible.

Include axis units, population definitions, sample/ROI selection, color
legends, and denominators in figure captions. For reconstructed tissues,
explain that the visualization uses cell measurements at centroid positions.

Analysis records
----------------

Keep the following with exported results:

* Application release and original input-file identifiers.
* Exposure metadata, annotation tables, and join keys.
* Marker/localization choices, filtering thresholds, and retained cell counts.
* Background-correction and normalization settings, including reference cells.
* Threshold CSV and phenotype-tree JSON files.
* Area method, resolution, and quantitative grouping choices.
* Grid rules, neighbor and cluster counts, sampling, and random seeds.

Record settings manually when your release does not provide an export for
them. Do not assume a processed table or phenotype tree contains the entire
analysis state.

Resume or transfer an analysis
------------------------------

Load the exported table corresponding to the stage you need, check its
identifiers and columns, and reuse compatible threshold/tree definitions.
Confirm the expected data scale before applying them.

Verify row counts, population counts, and a representative plot against the
previous result. A CSV export does not necessarily restore every interface
selection or fitted analysis.
