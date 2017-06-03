#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# (c) 2017, Vitaliy Zhydchenko <>
#
# This file is part of CloudBay
#
# CloudBay is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# CloudBay is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with CloudBay.  If not, see <http://www.gnu.org/licenses/>.

########################################################

from __future__ import with_statement

import sys

from setuptools import setup, find_packages


with open('README') as f:
    readme = f.read()

long_description = """
You can also install the `development version via ``pip install -e
git+https://github.com/Striker007/gscale/#egg=gscale``.

----

%s

----

For more information, please see the CloudBay website or execute ``fab --help``.
""" % (readme)


with open('requirements.txt') as f:
    install_requires = f.read().splitlines()


setup(
    name='Fabric',
    version='0.0.5',
    description='CloudBay is a simple, Pythonic tool for remote AWS Spot instence createing.',
    long_description=long_description,
    author='Vitaliy Zhydchenko',
    author_email='',
    url='https://github.com/Striker007/gscale',
    packages=find_packages(),
    test_suite='nose.collector',
    tests_require=['nose<2.0', 'fudge<1.0', 'jinja2<3.0'],
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'cloud-daemon=cloud_bay.main:main',
        ]
    },
    classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: BSD License',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Unix',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.5',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Topic :: Software Development',
          'Topic :: Software Development :: Build Tools',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: System :: Clustering',
          'Topic :: System :: Software Distribution',
          'Topic :: System :: Systems Administration',
    ],
)
