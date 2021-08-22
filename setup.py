# -*- coding: utf-8 -*-

from os import path

from setuptools import find_packages, setup

# Version
with open(path.join(path.dirname(__file__), "prosegrinder", "VERSION")) as version_file:
    VERSION = version_file.read().strip()
# Long Description
with open(path.join(path.dirname(__file__), "README.rst")) as readme_file:
    LONG_DESCRIPTION = readme_file.read()

setup(
    name="prosegrinder",
    version=VERSION,
    description="A text analytics library for prose fiction.",
    long_description=LONG_DESCRIPTION,
    author="David L. Day",
    author_email="dday376@gmail.com",
    url="https://github.com/prosegrinder/python-prosegrinder",
    packages=find_packages(include=["prosegrinder", "prosegrinder.*"]),
    entry_points={
        "console_scripts": [
            "prosegrinder = prosegrinder.__main__:cli",
        ],
    },
    package_dir={"prosegrinder": "prosegrinder"},
    package_data={
        "": ["LICENSE", "*.rst", "MANIFEST.in"],
    },
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    install_requires=[
        "cmudict>=1.0.0",
        "narrative>=1.0.0",
        "pointofview>=1.0.0",
        "syllables>=1.0.0",
        "click>=8.0.1",
    ],
    python_requires=">=3.6",
)
