Export and document the ctTMA run
================================================

**Input:** results from the preceding tutorial steps.

Save tables, figures, and definitions
-------------------------------------

1. Export processed and classified tables and quantitative/spatial results.
2. Save figures with readable labels, legends, and physical units.
3. Export thresholds and the phenotype tree.
4. Record settings not included in exported files.

Use :doc:`../exports` as the reproducibility checklist.

.. admonition:: Screenshot to add

   Capture the export controls and the resulting output directory, hiding
   personal paths. Show representative output filenames from this run.

Verify the saved analysis
-------------------------

Open exported tables and figures. Compare row/population counts with the
interface and confirm the selected ROI and marker labels.

Keep a run record containing the application and dataset versions, input
filenames, filtering counts, normalization choices, threshold values, tree,
area/resolution settings, and spatial parameters.

Completing the illustrated example
----------------------------------

Replace each screenshot slot with an actual capture from this same ctTMA run,
using a Sphinx ``figure`` directive, descriptive alternative text, and a
caption identifying the inputs and settings shown. Store documentation
screenshots under ``docs/source/_static/cttma/`` and reference them relative
to the source root, for example ``/_static/cttma/01-project-settings.png``.

Before calling the tutorial a reproducible reference, add the measured
checkpoints and confirm that a second run using the recorded settings
produces the expected outputs. No application screenshots or numerical
reproduction results are supplied by this draft.
