#!/usr/bin/env python
#
# Copyright 2018-2023 contributors to the Marquez project
# SPDX-License-Identifier: Apache-2.0
#
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()

requirements = [
    "requests",
    "six",
    "pyrfc3339",
    "deprecation",
    "pytz",
]

extras_require = {
    "tests": ["pytest", "pytest-cov", "mock", "flake8"],
}
extras_require["dev"] = set(sum(extras_require.values(), []))

setup(
    name="marquez-python",
    version="0.51.2",
    description="Marquez Python Client",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Marquez Project",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    extras_require=extras_require,
    python_requires=">=3.6",
    zip_safe=False,
    keywords="marquez",
)
