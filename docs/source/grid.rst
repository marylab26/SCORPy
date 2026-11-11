Grid analysis
================

Construction and region rules
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

