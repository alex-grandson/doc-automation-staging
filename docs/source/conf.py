# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------
import os
import sys
import datetime

sys.path.insert(0, os.path.abspath("../.."))

# -- Project information -----------------------------------------------------

today = datetime.date.today()
year = today.year

project = "Yadro Tryout"
copyright = f"{year}, Alexey Kutsenko"
author = "Alexey Kutsenko"

# -- Variables -----------------------------------------------------

# The full version, including alpha/beta/rc tags
release = (
    "0.1.0" if os.getenv("RELEASE_VERSION") is None else os.getenv("RELEASE_VERSION")
)
repo = "" if os.getenv("REPO_URL") is None else os.getenv("REPO_URL")

# -- General configuration ---------------------------------------------------

extensions = [
    "m2r",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx.ext.autodoc",
]

variables_to_export = ["release", "repo"]

templates_path = ["_templates"]

exclude_patterns = [".DS_Store", ".venv"]

source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "markdown",
}

numpydoc_show_class_members = False

# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_rtd_theme"

html_static_path = ["_static"]

rst_epilog = f"""
.. |ProjectVersion| replace:: RELEASE: {release}
.. |Repo| replace:: Link to `GitHub Repo`_. \n.. _GitHub Repo: {repo}
"""
