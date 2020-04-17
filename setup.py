#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(name='nbimporter',
      version='0.3.2',
      description='Import IPython notebooks as modules',
      author='Gregor Sturm',
      author_email='mail@gregor-sturm.de',
      py_modules=['nbimporter', 'display_nb'],
      license="BSD 3-clause",
      url='https://github.com/grst/nbimporter',
      setup_requires=["wheel", "setuptools"]
 )
