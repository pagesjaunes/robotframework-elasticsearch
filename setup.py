#!/usr/bin/env python

"""Setup script for Robot's ElasticSearch distributions"""

from distutils.core import setup
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
from ElasticSearchLib import __version__

def main():
	setup(name = 'robotframework-elasticsearch',
		version = __version__,
		description = 'ElasticSearch library for Robot Framework',
		author = 'PagesJaunes',
		author_email = 'fdepaulis@pagesjaunes.fr',
		url = 'https://github.com/pagesjaunes/robotframework-elasticsearch',
		package_dir = { '' : 'src'},
		packages = ['ElasticSearchLib'],
		requires = ['robotframework','elasticsearch']
	)

if __name__ == "__main__":
	main()