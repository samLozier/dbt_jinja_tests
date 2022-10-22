"""Sphinx configuration."""
project = "Dbt_Jinja_Tests"
author = "Samuel Lozier"
copyright = "2022, Samuel Lozier"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
