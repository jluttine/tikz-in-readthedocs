TikZ support in Read the Docs service
=====================================

.. tikz:: A beautiful TikZ drawing which works in readthedocs.org.

   \draw[thick,rounded corners=8pt]
   (0,0)--(0,2)--(1,3.25)--(2,2)--(2,0)--(0,2)--(2,2)--(0,0)--(2,0);


TikZ extension for Sphinx
-------------------------

Sphinx is a document generator, which can output, for instance, PDF and HTML.
Often, the documentation contains some illustration. It would be nice to have
the code of the figures in your documentation source files, so it is easy to
edit the graphics and you don’t need to manually generate any external image
files. Also, it’s good to have the graphics automatically in a proper format for
both PDF and HTML outputs. For this purpose, TikZ is a great LaTeX package for
drawing vector graphics. With a TikZ extension for Sphinx, you can use TikZ
syntax directly in the documentation source files to generate graphics. The
output is native in PDF output and PNG images in HTML output.

The TikZ extension for Sphinx can be installed as:

.. code-block:: console

   pip install sphinxcontrib-tikz

Note that Sphinx and its extensions must be installed to the same virtual
environment. If Sphinx is installed to the system directories, it won't find
extensions that are in virtual environments.

In your `conf.py`, add the TikZ extension to the list of enabled extensions:

.. code-block:: python

   extensions = ['sphinxcontrib.tikz']

Also, add the following lines to support TikZ in PDF output:

.. code-block:: python

   latex_elements = {
   'preamble': '\usepackage{tikz}',
   }

Now you should be able to build your documentation to PDF and HTML using Sphinx
and the TikZ graphics should show nicely.


Making it work at Read the Docs
-------------------------------

Readthedocs.org is a free service for sharing your documentation in various
formats. If you are using GitHub for your projects, it is easy to share
up-to-date documentation automatically in readthedocs.org.

However, if you try to build your documentation using TikZ in readthedocs.org,
it builds PDF successfully but fails to build HTML. It complains about a missing
file:

.. code-block:: none

   WARNING: pdftoppm command cannot be run

This package provides a fix for that. Just add `rtd-tikz` to your requirements
file that is used by Read the Docs, and everything should work (if it worked
locally).

GitHub repository: https://github.com/jluttine/tikz-in-readthedocs
