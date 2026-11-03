Thresholds and cell phenotyping
===============================

Define marker positivity
------------------------

Load the dataset at the intended processing stage and open **Thresholds**.
Use bivariate expression plots to examine separation between marker-positive
and marker-negative populations, comparing mutually exclusive markers where
biologically appropriate.

Adjust each threshold while checking the highlighted cells. Record the data
scale on which thresholds were defined: a threshold from normalized data
cannot be applied directly to raw intensity values.

Validate in tissue context
--------------------------

Inspect marker-positive cells in the digital tissue reconstruction for
individual samples and ROIs. Compare their locations with the original
fluorescence images when available.

Spillover, segmentation errors, and tissue autofluorescence can produce
apparently positive cells. A visually separated population is not sufficient
validation by itself.

Build a phenotype library
-------------------------

In **Cell Classification**, build a hierarchical decision tree. Begin with
major compartments, then add subtypes using marker combinations.

For example, an immune compartment can be defined using CD45 and then
subdivided using lineage markers. These are dataset-specific biological
rules, not universal phenotype definitions. Select markers and names
appropriate to the tissue, species, and antibody panel.

Review the classification on expression plots and tissue reconstructions,
including cells assigned to default populations.

Rule logic, priority, and defaults
----------------------------------

When more than one marker is involved in a rule defining a phenotype, SCORPy evaluates the
AND/OR marker conditions (OR by default) and depth-first, left-to-right traversal priority. 
The first matching sibling rule takes priority; unmatched cells receive a configurable default label.

Consequently, overlapping rules can produce different assignments when
reordered. Check sibling priority, default labels, and ambiguous marker
combinations explicitly. Root-level classes represent cell types; deeper
levels refine subtypes.

Save and reuse definitions
--------------------------

Export thresholds and the phenotype tree, retaining them with the classified
dataset and application version. Thresholds are saved in CSV
format and classification trees in JSON format.

Before reusing definitions, confirm the marker names, localization,
processing scale, and biological context. Revalidate on the new dataset
rather than assuming thresholds transfer unchanged.

**Outputs:** classified cells, threshold definitions, and a reusable
phenotype library. **Next:** :doc:`analysis` or :doc:`spatial`.
