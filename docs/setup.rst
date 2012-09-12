Setup
=====

.. tikz:: A beautiful TikZ drawing which works in readthedocs.org.

   \draw[thick,rounded corners=8pt]
   (0,0)--(0,2)--(1,3.25)--(2,2)--(2,0)--(0,2)--(2,2)--(0,0)--(2,0);


Readthedocs.org is a free service for sharing your documentation in
various formats. If you are using github for your projects, it is easy
to share up-to-date documentation automatically in
readthedocs.org. The underlying documentation generator is Sphinx,
which can output, for instance, PDF and HTML.

Often, the documentation contains some illustration. It would be nice
to have the code of the figures in your documentation source files, so
it is easy to edit the graphics and you don’t need to manually
generate any external image files. Also, it’s good to have the
graphics automatically in a proper format for both PDF and HTML
outputs. For this purpose, TikZ is a great LaTeX package for drawing
vector graphics. With a TikZ extension for Sphinx, you can use TikZ
syntax directly in the documentation source files to generate
graphics. The output is native in PDF output and PNG images in HTML
output.

The installation of the TikZ extension for Sphinx is easy with the
instructions
(http://people.ee.ethz.ch/~creller/web/tricks/sphinx-tikz.html).  For
Ubuntu, install texlive, texlive-pictures, poppler-utils, and netpbm
or imagemagick. Copy tikz.py to your documentation source directory
and add the path to conf.py:

.. code-block::
   
   sys.path.insert(0, os.path.abspath('.'))

Here we assumed that tikz.py lies in the same folder as conf.py. Also, use TikZ package for LaTeX when generating PDF:

.. code-block::

   latex_elements = {
   'preamble': '\usepackage{tikz}',
   }

Now you should be able to build your documentation to PDF and HTML
using Sphinx and the TikZ graphics should show nicely.

However, if you try to build your documentation in readthedocs.org, it
builds PDF successfully but fails to build HTML. It complains about a
missing file:

.. code-block::

   WARNING: pdftoppm command cannot be run

Actually, this isn’t the only file missing: there are three
executables (pdftoppm, pnmcrop, pnmtopng) and one library
(libnetpbm.so.10) missing. These files are missing from the
readthedocs.org server. Fortunately, the server is running Linux, so
it is possible to get these binaries from another Linux computer and
add them to the repository. Once you have obtained the binaries, put
them into your documentation source. Let’s assume you put them in
folder _bin) under the documentation source folder (i.e., the folder
where conf.py lies).

However, readthedocs.org doesn’t look for executable nor libraries
from your repository. Therefore, you need to add their paths to the
environment variables. In conf.py, add the following:

.. code-block::
  
   if os.environ.get('READTHEDOCS', None) == 'True':
       os.environ["PATH"] += os.pathsep + os.path.abspath('_bin')
       os.environ["LD_LIBRARY_PATH"] = os.path.abspath('_bin')

Now readthedocs.org should build both PDF and HTML successfully with
beautiful TikZ graphics.

For making it easier to use this setup, I created a dummy Github
repository, which contains the required files and configuration. The
repository is located at
https://github.com/jluttine/tikz-in-readthedocs and the resulting
outputs in readthedocs.org are located at
http://tikz-in-readthedocs.readthedocs.org. Feel free to use them.
