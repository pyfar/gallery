# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import re
# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

project = 'pyfar gallery'
copyright = '2024, The pyfar developers'
author = 'The pyfar developers'
release = '0.1.0'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'matplotlib.sphinxext.plot_directive',
    'sphinx.ext.mathjax',
    'sphinx.ext.intersphinx',
    'sphinx_gallery.load_style',
    'nbsphinx',
    'autodocsumm',
    "sphinx_design",
    "sphinx_favicon",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# default language for highlighting in source code
highlight_language = "python3"

# intersphinx mapping
intersphinx_mapping = {
    'numpydoc': ('https://numpydoc.readthedocs.io/en/stable/', None),
    'pytest': ('https://docs.pytest.org/en/stable/', None),
    'coverage': ('https://coverage.readthedocs.io/en/latest/', None),
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_css_files = ['css/custom.css']
html_logo = 'resources/logos/pyfar_logos_fixed_size_pyfar.png'
html_title = "pyfar"
html_favicon = '_static/favicon.ico'


# -- HTML theme options
# https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/layout.html

html_theme_options = {
    "navbar_start": ["navbar-logo"],
    "navbar_end": ["navbar-icon-links", "theme-switcher"],
    "navbar_align": "content",
    "header_links_before_dropdown": 5,  # manual set
    "header_dropdown_text": "Packages",  # Change dropdown name from "More" to "Packages"
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/pyfar",
            "icon": "fa-brands fa-square-github",
            "type": "fontawesome",
        },
        {
            "name": "CC-BY",
            "url": "https://creativecommons.org/licenses/by/4.0/deed.de",
            "icon": "fa-brands fa-creative-commons-by",
            "type": "fontawesome",
        }
    ],
    # Configure secondary (right) side bar
    "show_toc_level": 3,                     # Show all subsections of notebooks
    "show_nav_level": 2,
    "secondary_sidebar_items": ["page-toc"]  # Omit 'show source' link that that shows notebook in json format
}

# -- Options for nbsphinx -------------------------------------------------
nbsphinx_prolog = r"""
{% set docname = 'docs/' + env.doc2path(env.docname, base=None)|string %}

.. raw:: html

    <div class="admonition note">
      {% if "gallery/no_binder/" in docname %}
      This example must be run locally, please
      {% else %}
      Open an interactive online version by clicking the badge
      <span style="white-space: nowrap;"><a href="https://mybinder.org/v2/gh/pyfar/gallery/main?labpath={{ docname|e }}"><img alt="Binder badge" src="https://mybinder.org/badge_logo.svg" style="vertical-align:text-bottom"></a></span>
      or
      {% endif %}
      <a href="{{ env.docname.split('/')|last|e + '.ipynb' }}" class="reference download internal" download>download</a>
      the notebook.
      <script>
        if (document.location.host) {
          let nbviewer_link = document.createElement('a');
          nbviewer_link.setAttribute('href',
            'https://nbviewer.org/url' +
            (window.location.protocol == 'https:' ? 's/' : '/') +
            window.location.host +
            window.location.pathname.slice(0, -4) +
            'ipynb');
          nbviewer_link.innerHTML = 'Or view it on <em>nbviewer</em>';
          nbviewer_link.classList.add('reference');
          nbviewer_link.classList.add('external');
          document.currentScript.replaceWith(nbviewer_link, '.');
        }
      </script>
    </div>

"""

# replace examples_gallery hard link to internal link
with open("_static/header.rst", "rt") as fin:
    with open("header.rst", "wt") as fout:
        for line in fin:
            new_line = line
            for version in ['latest', 'stable']:
                pattern = fr'(https://pyfar-gallery\.readthedocs\.io/en/{version}/(.*?)\.html)'
                match = re.search(pattern, new_line)
                if match:
                    new_line = re.sub(pattern, match.group(2), new_line)
            fout.write(new_line)


# -- manage thumbnails --------------------------------------------------------
# must be located in 'docs/_static'
nbsphinx_thumbnails = {
    'gallery/interactive/pyfar_audio_objects': '_static/thumbnail_pyfar_audio_objects.png',
    'gallery/interactive/pyfar_coordinates': '_static/thumbnail_pyfar_coordinates.png',
    'gallery/interactive/pyfar_filter_types': '_static/thumbnail_pyfar_filter_types.png',
    'gallery/interactive/pyfar_arithmetics': '_static/thumbnail_pyfar_arithmetics.png',
    'gallery/interactive/pyfar_filtering': '_static/thumbnail_pyfar_filtering.png',
    'gallery/interactive/sofar_introduction': '_static/thumbnail_sofar_introduction.png',
    'gallery/interactive/fast_fourier_transform': '_static/thumbnail_fast_fourier_transform.png',
    'gallery/interactive/pyfar_introduction': '_static/pyfar_pf_transparent.png',
    'gallery/interactive/pyfar_interactive_plots' : '_static/thumbnail_pyfar_interactive_plots.png',
}
