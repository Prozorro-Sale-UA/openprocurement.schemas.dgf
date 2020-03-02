from setuptools import setup, find_packages
import os

version = '1.2.3'

requires = [
    'setuptools',
    'schematics',
    'jsonschema==2.6.0'
]

test_requires = requires + [
    'flake8',
    'coverage',
    'Sphinx',
    'mock'
]

docs_requires = requires + [
    'sphinxcontrib-httpdomain',
    'sphinx_rtd_theme',
    'sphinx-jsonschema'
]


here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md')) as f:
    README = f.read()

setup(name='openprocurement.schemas.dgf',
      version=version,
      description="",
      long_description=README,
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        ],
      keywords="web services",
      author='Quintagroup, Ltd.',
      author_email='info@quintagroup.com',
      url='https://github.com/openprocurement/openprocurement.schemas.dgf',
      license='Apache License 2.0',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['openprocurement', 'openprocurement.schemas'],
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      extras_require={'test': test_requires, 'docs': docs_requires},
      test_suite="openprocurement.schemas.dgf.tests.main.suite")
