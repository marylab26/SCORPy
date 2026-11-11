Set thresholds and classify cells
================================================

**Input:** the processed table from :doc:`preprocessing`.

Inspect marker thresholds
-------------------------

At this stage, you have likely completed the filtering and 
normalization steps and saved the normalized data in the `normalization/` 
folder (see :doc:`preprocessing`). 
You can therefore import the normalized data directly and 
proceed to inspect it and set the marker thresholds for cell classification.

.. video:: ../../../resources/ctTMA_Thresholds1.mp4
   :width: 100%
   :align: center



Adjust positivity thresholds using the expression plots and inspect positive 
cells in each selected tissue reconstruction.

.. admonition:: Important

   Compare with original fluorescence images when available. Don't forget to save the threshold values.


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
