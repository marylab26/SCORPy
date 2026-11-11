Neighborhood analysis
================

Neighborhood analysis: nearest-target cell distances
-----------------------------

In **Neighborhood Analysis**, select source and target cell populations to
compare distances between their centroids within each ROI.

Euclidean distance to the nearest target cell is used.
A displayed reference distance is not a cutoff that removes more distant
cells from that distribution. 

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
