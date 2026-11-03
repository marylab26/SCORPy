Spatial analysis
================

Coordinates, units, and tissue boundaries
-----------------------------------------

Use a dataset with spatial coordinates and the population labels or marker
variables required for your question. Set the imaging resolution to the
actual acquisition pixel size before interpreting physical distances.

Keep distinct tissues separated by sample/ROI identifiers. Spatial calculations within individual ROIs, not across
discontinuous tissue cores. 

Grid construction and region rules
----------------------------------

In **Grid Analysis**, choose a grid scale appropriate to the tissue. The
manuscript describes fixed pixel dimensions or dimensions adapted to a
target number of cells per grid.

Define region labels using population proportions, binary marker variables,
mean expression, or composite AND/OR conditions. Rules are ordered:
the first matching rule assigns the label, and unmatched grids receive a
default label.

Inspect the grid overlay and test whether the interpretation changes with
grid size or rule priority. A grid labeled epithelial-rich is a
composition-based region, not an independently segmented epithelial mask.

Distance from reference regions
-------------------------------

Choose a grid class as the reference and inspect the resulting proximity map
and distance-resolved population summaries.

Chebyshev distances on the grid are used, using
eight-connected neighbors. Grid-step proximity is distinct from direct
cell-to-cell Euclidean distance. Report grid dimensions, resolution, source
class, and any distance bins with the result.

Nearest-target cell distances
-----------------------------

In **Neighborhood Analysis**, select source and target cell populations to
compare distances between their centroids within each ROI.

Euclidean distance to the nearest target cell is used.
A displayed reference distance is not a cutoff that removes more distant
cells from that distribution. Check source and target presence in each ROI
before interpreting the summaries.

Short distances indicate spatial proximity, not proof of physical contact
or a functional interaction.

Cellular neighborhood clustering
--------------------------------

Select the cell labels, number of nearest neighbors, and number of clusters.
Construct a local cell-type composition vector
for each cell, log1p-transforming those vectors, and grouping them using
k-means.

The neighbor count controls the local context; the cluster count controls
how many neighborhood groups are formed. These are different parameters.
Inspect both neighborhood composition profiles and their spatial maps, and
compare plausible parameter choices.

Cluster labels are analysis-specific and should not be assumed to match
between independently fitted runs.

**Outputs:** grid classes, proximity results, nearest-target distributions,
and cellular neighborhood maps. See :doc:`exports` for reporting records.
