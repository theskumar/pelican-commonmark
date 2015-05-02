# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

import os
import sys

from setuptools import setup, find_packages

VERSION = '0.1.0'

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a v%s -m 'version %s'" % (VERSION, VERSION))
    print("  git push --tags")
    sys.exit()

setup(
    name='pelican-commonmark',
    version=VERSION,
    author='Saurabh Kumar',
    author_email='me@saurabh-kumar.com',
    include_package_data=False,
    packages=find_packages(exclude=['*tests*']),
    install_requires=[
        'pelican>=3.5.0',
        'CommonMark>=0.5.4',
    ],
    url='https://github.com/theskumar/pelican-commonmark',
    license='BSD licence, see LICENCE.txt',
    description='This reader plugin replaces the markdown reader with one that uses the Python parser for CommonMark',

    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
