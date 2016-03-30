TikZ in readthedocs.org
=======================

This package contains binary files (executables and libraries) that are needed
for `sphinxcontrib-tikz` package but are missing from readthedocs.org. This
enables documentations created with Sphinx to use TikZ drawings at
readthedocs.org.

To enable the TikZ support at readthedocs.org, add `rtd-tikz` to the
requirements file used by readthedocs.org.

GitHub repository: https://github.com/jluttine/tikz-in-readthedocs

**WARNING:** You probably want to install this package into a virtual
environment, otherwise you may accidentally overwrite your system binaries if
you have them.


License
-------

* bin/pdftoppm
   * License: GPLv2 or GPLv3
   * Source: https://cgit.freedesktop.org/poppler/poppler

* bin/pnmcrop
   * Copyright (C) 1989 by Jef Poskanzer.
   * License: GPLv2, MIT
   * Source: https://sourceforge.net/projects/netpbm/

* bin/pnmtopng
   * Copyright (C) 1995-1997 by Alexander Lehmann and Willem van Schaik
   * License: Open source
   * Source: https://sourceforge.net/projects/netpbm/

* lib/libnetpbm.so.10
   * License: GPLv2, MIT
   * Source: https://sourceforge.net/projects/netpbm/

* All other files
   * Copyright (C) 2012, 2016 by Jaakko Luttinen
   * License: MIT
