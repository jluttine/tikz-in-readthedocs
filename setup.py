#!/usr/bin/env python

################################################################################
# Copyright (C) 2016 Jaakko Luttinen
#
# This file is licensed under the MIT License.
################################################################################


NAME         = 'rtd-tikz'
DESCRIPTION  = 'Binaries in order to use Sphinx TikZ extension at Read the Docs'
AUTHOR       = 'Jaakko Luttinen'
AUTHOR_EMAIL = 'jaakko.luttinen@iki.fi'
URL          = 'http://tikz-in-readthedocs.readthedocs.org'
LICENSE      = 'Various open source licenses'
VERSION      = '0.1.1'
COPYRIGHT    = '2012-2016, Jaakko Luttinen'


if __name__ == "__main__":

    import os

    # Utility function to read the README file.
    # Used for the long_description.  It's nice, because now 1) we have a top level
    # README file and 2) it's easier to type in the README file than to put a raw
    # string in below ...
    def read(fname):
        return open(os.path.join(os.path.dirname(__file__), fname)).read()

    from setuptools import setup, find_packages

    setup(
        packages         = [],
        install_requires = [],
        data_files       = [
            (
                'bin',
                [
                    'bin/pdftoppm',
                    'bin/pnmcrop',
                    'bin/pnmtopng',
                ]
            ),
            (
                'lib',
                [
                    'lib/libnetpbm.so.10',
                ]
            )
        ],
        name             = NAME,
        version          = VERSION,
        author           = AUTHOR,
        author_email     = AUTHOR_EMAIL,
        description      = DESCRIPTION,
        license          = LICENSE,
        url              = URL,
        long_description = read('README.rst'),
        keywords         = [
            'TikZ',
            'Sphinx',
            'Read the Docs',
            'RTD',
        ],
        classifiers = [
            'Programming Language :: Python',
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved',
            'Operating System :: OS Independent',
            'Topic :: Scientific/Engineering :: Visualization',
        ],
    )

