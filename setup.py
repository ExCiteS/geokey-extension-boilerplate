#!/usr/bin/env python

from os.path import join
from setuptools import setup, find_packages


name = 'geokey-extension-boilerplate'
version = __import__(name.replace('-', '_')).__version__
repository = join('https://github.com/ExCiteS', name)

setup(
    name=name,
    version=version,
    description='Boilerplate repository for GeoKey extensions',
    url=repository,
    download_url=join(repository, 'tarball', version),
    author='ExCiteS',
    author_email=' excites@ucl.ac.uk',
    license='MIT',
    packages=find_packages(exclude=['*.tests', '*.tests.*', 'tests.*']),
    include_package_data=True,
    install_requires=[],
)
