Set thresholds and classify cells
================================================

**Input:** the processed table from :doc:`preprocessing`.

Inspect marker thresholds
-------------------------

1. Open **Thresholds** and select a marker pair appropriate to your panel.
2. Adjust positivity thresholds using the expression plots.
3. Inspect positive cells in each selected tissue reconstruction.
4. Compare with original fluorescence images when available.

Save the threshold values and record the scale on which they were defined.
The Zenodo file list does not include a separate threshold CSV; do not assume
one is available or that loading a tree restores every threshold setting.

.. admonition:: Screenshot to add

   Show a marker pair with its thresholds and the corresponding tissue
   reconstruction. Include marker names and the selected sample/ROI.

Load and review the example tree
--------------------------------

1. Open **Cell Classification**.
2. Import ``reference/ctTMA_cell_tree.json`` using the available tree-import
   control.
3. Review marker names, logical conditions, sibling priority, and defaults.
4. Confirm compatibility with the active table and threshold definitions
   before applying classification.

See :doc:`../classification` for rule evaluation and phenotype validation.
The supplied tree is a reference for this dataset, not a universal library.

.. admonition:: Screenshot to add

   Capture the imported phenotype hierarchy and a classified tissue view,
   including the legend and default/unassigned populations.

Check before continuing
-----------------------

Inspect major compartments and finer subtypes in expression and tissue
context. Record population counts and save the thresholds, tree, and
classified table. Do not assume that a newly processed run reproduces
``ctTMA_classified.csv`` without checking processing choices.

**Next:** :doc:`analysis`.
