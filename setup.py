#!/usr/bin/env python

import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open(os.path.join(os.path.dirname(__file__), "README.md"), encoding="UTF-8") as f:
    readme = f.read()

version = "0.0.4"
package_data = {}
setup(
    name="ember-mivia",
    version=version,
    url = "https://github.com/gparrella12/ember",
    long_description_content_type = "text/markdown",
    description="Endgame Malware BEnchmark for Research",
    long_description=readme,
    packages=["ember"],
    package_data=package_data,
    author_email="proth@endgame.com")
