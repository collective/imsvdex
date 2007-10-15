from setuptools import setup, find_packages
import sys, os

version = '1.0'

setup(name='imsvdex',
      version=version,
      description="Read and write vocabularies in Vocabulary Definition Exchange format specified by imsglobal.org.",
      long_description="""\
todo""",
      classifiers=[], # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      keywords='vocabulary xml',
      author='Martin Raspe',
      author_email='raspe@biblhertz.it',
      url='',
      license='D-FSL - German Free Software License',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
      
