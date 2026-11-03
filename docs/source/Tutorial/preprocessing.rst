Clean and normalize the ctTMA data
================================================

**Input:** the raw table and metadata loaded in :doc:`import`.

Select measurements and filter cells
------------------------------------

1. Open **Cleaning** and choose the markers and subcellular localizations.
2. Inspect nuclear size and autofluorescence distributions by sample/ROI.
3. Set filtering thresholds based on those distributions and tissue context.
4. Apply cleaning and record retained and removed cell counts.

.. admonition:: Screenshot to add

   Show marker/localization selection, filter values, distributions, and
   before/after cell counts from the same run.

Correct background and normalize
---------------------------------

1. Open **Normalization**.
2. Confirm marker-to-autofluorescence matching and the exposure metadata.
3. Apply the intended background correction and normalization.
4. Inspect raw versus normalized distributions and a heatmap grouped by
   available tissue annotations.

Use :doc:`../preprocessing` for the method and assumptions. Do not substitute
guessed exposure times when a mapping is missing.

.. admonition:: Screenshot to add

   Capture the correction settings and comparable raw/normalized views.
   Keep marker names, legends, and data scales readable.

Check before continuing
-----------------------

Record marker selections, filter thresholds, correction settings, and output
location. Confirm that recognizable tissue-specific expression patterns remain.
Exact values and expected cell counts must come from the documented run.

**Next:** :doc:`classification`.
