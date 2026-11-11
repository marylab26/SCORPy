Quality control and normalization
=================================

Marker and localization selection
---------------------------------

In **Cleaning**, select the markers and subcellular localizations relevant
to your biological question. For example, nuclear marker and membrane
markers are not expected in the same compartment.

Review the retained columns before continuing. DAPI columns, empty or unassigned channels, and intensity 
columns outside the selected marker/localization set are removed during automated cleaning.

Inspect and filter cells
------------------------

Use distributions and bivariate plots to inspect nuclear size,
autofluorescence, and other numeric measurements. Adjust filters to exclude
likely segmentation artefacts or abnormal signals.

Extreme nuclear sizes may indicate segmentation problems, while strong
autofluorescence can obscure marker measurements. Neither criterion is
automatically proof that a cell is invalid. Compare filtering decisions with
the tissue and record the thresholds and number of cells removed.

Inspect each sample or ROI, not only the pooled distribution, so that a
filter does not unintentionally remove a particular biological population.

Exposure-aware background correction
------------------------------------

In **Normalization**, check marker-to-autofluorescence matching and exposure
metadata before applying the correction.

.. math::

   I_{\mathrm{corr}} =
   \frac{I_{\mathrm{marker}}}{t_{\mathrm{marker}}}
   - \frac{I_{\mathrm{AF}}}{t_{\mathrm{AF}}}

Here, the two exposure times correspond to their respective measurements;
the autofluorescence signal is matched to the relevant channel and compartment.
See :doc:`settings` for metadata preparation.

Compare distributions and tissue reconstructions before and after correction.
If the necessary autofluorescence or exposure measurements are absent, do not
treat the dataset as though this correction had been performed.

Log transformation and normalization
------------------------------------

Then, SCORPy applies log2 transformation, with non-positive corrected
values set to a floor of 0.1 before taking the logarithm, followed by
marker-wise median-centered z-scoring:

.. math::

   z_{ij} =
   \frac{\log_2(x_{ij}) -
   \operatorname{median}_i(\log_2(x_{ij}))}
   {\operatorname{SD}_i(\log_2(x_{ij}))}

Normalized values express relative signal on a dimensionless scale, not
absolute protein abundance. Check constant or otherwise uninformative
markers before interpreting normalized measurements.


**Next:** :doc:`classification`.
