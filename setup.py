from __future__ import print_function
import sys
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    INSTALL_REQUIRES = [l.strip() for l in f.readlines() if l]


setup(name='stability-selection',
      version='0.0.1',
      description='A scikit-learn compatible implementation of stability selection for feature selection',
      author='Thomas Huijskens',
      packages=find_packages(),
      install_requires=INSTALL_REQUIRES,
      author_email='thomas_huijskens@hotmail.com',
      )
