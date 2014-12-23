#!/usr/bin/env python

"""Setup script for Robot's ElasticSearch distributions"""

# from distutils.core import setup
# import sys, os
# sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
from setuptools import setup, find_packages
import ElasticSearchLib

def main():
	setup(
		name = 'robotframework-elasticsearch',
		version = ElasticSearchLib.__version__,
		description = 'ElasticSearch library for Robot Framework',
		author = 'PagesJaunes',
		author_email = 'fdepaulis@pagesjaunes.fr',
		url = 'https://github.com/pagesjaunes/robotframework-elasticsearch',
		packages=find_packages(),
		install_requires = ['robotframework','elasticsearch']
	)

if __name__ == "__main__":
	main()