#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

with open("requirements/requirements.txt", "r") as requirements_txt:
    requirements = requirements_txt.read().split("\n")

with open("requirements, requirements_dev.txt", "r") as requirements_txt:
    dev_requirements = requirements_txt.read().split("\n")

setup_requirements = [
    "pytest-runner",
]

test_requirements = dev_requirements

setup(
    author="Moritz Federspiel",
    author_email="moritz.federspiel@steadysense.at",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Sends emails from form POST requests",
    entry_points={"console_scripts": ["formmailer=formmailer.__main__:main"]},
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="formmailer",
    name="formmailer",
    packages=find_packages("src"),
    package_dir={"": "src"},
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/steadysense/formmailer",
    version="0.1.0",
    zip_safe=False,
)
