Marker analysis and quantification
==================================

Explore marker expression
-------------------------

Use **Marker Analysis** to inspect marker measurements within selected
cell types or subtypes. Compare continuous expression distributions with
threshold-based positivity and inspect spatial expression patterns in
digital tissue reconstructions.

These answer different questions: a shift in intensity need not imply the
same change as the fraction of cells above a chosen cutoff.

Generate binary marker variables
--------------------------------

Define marker positivity using a threshold and, when needed, a cell-type
constraint. Review which cells are included before generating binary
columns.

These variables can describe functional states within a population and
can be used in spatial grid rules or exported for other analyses.
Keep the threshold and population definition alongside the derived column.

Compare composition and annotation groups
-----------------------------------------

In **Quantification**, select the populations, samples/ROIs, and annotation
groups to compare. Inspect cell-type or subtype proportions and marker
expression summaries.

State the denominator of every reported proportion, such as all retained
cells or a selected parent population. Retain sample-level results rather
than reporting only pooled cell counts.

For statistical interpretation, distinguish cells from independent
biological replicates. Multiple ROIs from the same specimen are not
automatically independent samples.

Tissue area and cell density
----------------------------

Two area sources are available: an existing area measurement,
with unit conversion, or an estimate from the occupied spatial distribution
of cell centroids.

Check area units and imaging resolution before computing densities:

.. math::

   \mathrm{density} = \frac{\mathrm{cell\ count}}{\mathrm{tissue\ area}}

An area inferred from cell positions is an estimate, not a segmentation mask.
Its value depends on spatial binning and cell coverage; inspect it for
sparse tissue, holes, and disconnected regions. Record the area method.

UMAP and t-SNE
--------------

Choose the markers, cells, and embedding method. Record sampling size,
random state, and method-specific parameters when available. Compare
embeddings colored by phenotype, sample, and experimental group.

UMAP and t-SNE are dimensionality-reduction visualizations, not cell-type
classification or clustering algorithms. Separation in an embedding alone
does not validate a phenotype or establish a biological difference.

**Outputs:** quantitative tables, expression summaries, embeddings, and
figures. **Next:** :doc:`spatial` or :doc:`exports`.
