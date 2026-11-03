Reference and troubleshooting
=============================

Input and output reference
--------------------------

Use :doc:`settings` for intensity-header examples, annotation join keys,
and exposure-metadata requirements. The application's **Instruction** tab
and the manuscript's Tables are the sources for exposure examples
and column aliases.

This guide does not provide a complete accepted-header list or an importable
metadata template: those schemas require confirmation against a released
application. Do not infer a valid template from example filenames alone.

For output-directory purposes and records to retain, see :doc:`exports`.

Methods and limitations
-----------------------

The workflow guides explain the relevant methods:

* :doc:`preprocessing`: exposure correction, log transformation, and
  median-centered scaling.
* :doc:`classification`: thresholding and ordered hierarchical rules.
* :doc:`analysis`: area estimates, density, and dimensionality reduction.
* :doc:`spatial`: grid proximity, nearest-target distances, and
  composition-based neighborhoods.

Phenotypes depend on the marker panel, segmentation, thresholds, and rule
order. Spatial summaries depend on coordinates, resolution, sampling, and
parameter choices. Tissue reconstructions and expected marker patterns are
consistency checks, not independent cell-level ground truth.

Launch, import, and metadata problems
-------------------------------------

**The macOS application is blocked**
   Follow the trusted-download precautions in :doc:`installation`.

**CSV files fail validation**
   Check for empty files, duplicate column names, encoding problems, and
   incompatible table headers. Inspect the reported error rather than
   repeatedly merging the same files.

**Annotations are unmatched**
   Compare sample and ROI join keys, their formatting, missing values, and
   duplicate key combinations.

**Background correction appears incorrect**
   Check exposure units and marker-to-autofluorescence channel/localization
   mapping. Compare with the original measurements before changing thresholds.

**Spatial results have implausible units**
   Check whether coordinates are pixels or physical units, the acquisition
   resolution, and whether distinct tissues have been assigned distinct IDs.

**Large analyses are slow**
   Start with a sample/ROI subset and use sampling controls for visualization
   where available. Record sampling choices and do not confuse a visualization
   subset with full-dataset quantitative results.

Frequently asked questions
--------------------------

**Do I need Python?**
   Not for the pre-built Windows or macOS application.

**Does SCORPy segment images?**
   This workflow starts from post-segmentation single-cell tables.

**Can I skip preprocessing?**
   Yes, when the imported dataset is already appropriately processed.
   Check :doc:`installation` for entry points and downstream requirements.

**Are neighborhoods the same as nearest-target distances?**
   No. Distances describe proximity to a target population; neighborhood
   clustering groups cells by the composition of their local surroundings.

Citation, license, and support
------------------------------

Use the citation information in the
`repository README <https://github.com/marylab26/SCORPy#citation--acknowledgments>`_
when available; no publication identifier is assumed here.
Example data are linked at
`Zenodo <https://zenodo.org/records/22096493>`_.

SCORPy is distributed under the
`MIT license <https://github.com/marylab26/SCORPy/blob/main/LICENSE>`_.
Report problems through
`GitHub Issues <https://github.com/marylab26/SCORPy/issues>`_, including
the application version, operating system, workflow stage, and exact error.
Share only de-identified examples that you have permission to disclose.
