# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import os
import sys

# -- Project information -----------------------------------------------------

project = 'Pseudocerebellum'
copyright = '2020, Pentti Kanerva, Jeff Teeters, Bruno Olshausen'
author = 'Pentti Kanerva, Jeff Teeters, Bruno Olshausen'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
'sphinxcontrib.bibtex',
'sphinxcontrib.bibtex2',
'sphinxcontrib.bibtexpdflink',
'sphinxcontrib.filltableref',
]
bibtex_bibfiles = ['references/refs.bib']
bibtex_style = 'footapastyle'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# added for readthedocs
master_doc = 'index'

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/custom.css',
]

# these specify paths for sphinxcotrib-bibtexpdflink

bibtexpdflink_note_dir = "notes"
bibtexpdflink_pdf_dir = "papers"
