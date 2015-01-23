import os
del os.link

from distutils.core import setup

setup(
    # Application name:
    name="geokey-extension",

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="Your name",
    author_email="your-email@example.com",

    # Packages
    packages=["geokey_extension"],

    # Include additional files into the package
    include_package_data=True,

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    install_requires=[

    ],
)
