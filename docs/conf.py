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
sys.path.append(os.path.abspath("./_ext"))

# -- Project information -----------------------------------------------------

project = 'Pseudocerebellum'
copyright = '2019, Pentti Kanerva, Bruno Olshausen, Jeff Teeters'
author = 'Pentti Kanerva, Bruno Olshausen, Jeff Teeters'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
'lsphinxcontrib.bibtex',
'lsphinxcontrib.bibtex2',
]
bibtex_bibfiles = ['references/refs.bib']
bibtex_style = 'footapastyle'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


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

# -- Added for APA style
# -- from: sphinxcontrib-bibtex/test/issue77

from pybtex.style.formatting.unsrt import Style as UnsrtStyle
from pybtex.style.labels.alpha import LabelStyle as AlphaLabelStyle
from pybtex.plugin import register_plugin
import os
from pybtex.style.template import (
    href, optional, sentence, words
)
# extensions = ['sphinxcontrib.bibtex']
# exclude_patterns = ['_build']


class ApaLabelStyle(AlphaLabelStyle):
    def format_label(self, entry):
        # import pdb; pdb.set_trace()
        # from: https://stackoverflow.com/questions/55942749/how-do-you-change-the-style-of-pybtex-references-in-sphinx
        label = entry.key
        return label

class FootApaStyle(UnsrtStyle):
    def format_web_refs(self, e):
        # based on urlbst output.web.refs
        return sentence [
            optional [ self.format_url(e) ],
            optional [ self.format_eprint(e) ],
            optional [ self.format_pubmed(e) ],
            optional [ self.format_doi(e) ],
            # following added for pseudo cerebellum
            optional [ self.format_pdf(e) ],
            # optional [ self.format_rst(e) ],  # don't include rst link on footcite
            ]

    def format_pdf(self, entry):
        # create link to pdf file if present
        cwd = os.getcwd()
        print("%s - cwd = %s" % (entry.key, cwd))
        # last_part_path = os.path.basename(os.path.normpath(cwd))
        # if last_part_path == 
        pdf_name = entry.key + ".pdf"
        search_path = "./_static/papers/" + pdf_name
        if os.path.isfile(search_path):
            print("----------- Found %s", pdf_name)
            target_path = "../_static/papers/" + pdf_name
            return words [
                'pdf:',
                href [ target_path, pdf_name ]
            ]
        else:
            return words [""]


    def format_rst(self, entry):
        # create link to rst file if present
        rst_name = entry.key + ".rst"
        search_path = "./references/" + rst_name
        if os.path.isfile(search_path):
            html_name = entry.key + ".html"
            target_path = "../references/" + html_name
            print("----------- Found %s", rst_name)   
            return words [
                'Notes:',
                href [ target_path, html_name ]
            ]
        else:
            return words [""]

class ApaStyle(FootApaStyle):
    default_label_style = 'apa'

    def format_web_refs(self, e):
        # based on urlbst output.web.refs
        return sentence [
            optional [ self.format_url(e) ],
            optional [ self.format_eprint(e) ],
            optional [ self.format_pubmed(e) ],
            optional [ self.format_doi(e) ],
            # following added for pseudo cerebellum
            optional [ self.format_pdf(e) ],
            optional [ self.format_rst(e) ],   # include information about note page
            ]



register_plugin('pybtex.style.labels', 'apa', ApaLabelStyle)
register_plugin('pybtex.style.formatting', 'apastyle', ApaStyle)
register_plugin('pybtex.style.formatting', 'footapastyle', FootApaStyle)

