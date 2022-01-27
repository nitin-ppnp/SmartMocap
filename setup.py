#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='mcms',
      version='0.0.1',
      description='MCMS',
      author='Nitin Saini',
      author_email='nitin.saini@tuebingen.mpg.de',
      url='',
      install_requires=[
            'pytorch-lightning'
      ],
      packages=find_packages('src'),
      package_dir={'':'src'},
      )