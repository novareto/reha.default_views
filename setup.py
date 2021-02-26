#!/usr/bin/env python

"""The setup script."""

import codecs
import os
import re

from setuptools import setup, find_packages


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('docs/HISTORY.rst') as history_file:
    history = history_file.read()

requirements = "" 

setup_requirements = "" 

setup(
    name="reha.default_views",
    author="UV WEB Community",
    author_email="ck@novareto.de",
    version="0.1.0",
    description="Example Python namespace package.",
    long_description=readme + '\n\n' + history,
    long_description_content_type="text/x-rst",
    url="https://git.bg-kooperation.de",
    install_requires=requirements,
    include_package_data=True,
    packages=find_packages(include=['reha.default_views']),
    setup_requires=setup_requirements,
    entry_points={
        'fanstatic.libraries': [
            'reha.default_views  = reha.default_views.app:library',
        ],
        'docmanager.plugins': [
            'reha.default_views = reha.default_views'
        ],
    },
    test_suite='tests',
    zip_safe=False,
)
