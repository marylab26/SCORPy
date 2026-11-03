Quantify tissue composition and marker expression
================================================================

**Input:** your classified table from :doc:`classification`, or the provided
``ctTMA_classified.csv`` loaded as a separate downstream starting point.

Compare tissue composition
--------------------------

1. Open **Quantification** and inspect the available sample/ROI annotations.
2. Select cell types or subtypes and summarize composition by tissue.
3. Inspect one ROI separately, stating the denominator for each proportion.
4. Check area units and the area method before comparing cell densities.

.. admonition:: Screenshot to add

   Capture a composition plot with tissue labels and its associated table.
   For density results, also show the area method and units.

Explore a marker
----------------

1. Open **Marker Analysis** and select a marker present in the table.
2. Compare continuous expression across tissues or chosen populations.
3. Inspect a threshold-based positivity view and its tissue reconstruction.
4. If needed, create a binary variable for a clearly defined cell population.

Record the marker, localization, population filter, threshold, and selected
sample/ROI. For methodological details, see :doc:`../analysis`.

.. admonition:: Screenshot to add

   Show the marker distribution and matching spatial view, with the same
   marker, selected population, and ROI.

Check before continuing
-----------------------

Export the quantitative table and verify that it reflects your selected
groups. Preserve sample-level results rather than only pooled cell values.

**Next:** :doc:`spatial`.
