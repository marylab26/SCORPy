# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'SCORPy'
copyright = '2026, Zoé Gerber'
author = 'Zoé Gerber'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []
templates_path = ["_templates"]
exclude_patterns = []

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_logo = "../../resources/SCORPy_full_git.png"
html_favicon = "../../resources/SCORPy_icon.png"
html_theme_options = {
    "logo_only": True,
    "style_nav_header_background": "#ffffff",
}