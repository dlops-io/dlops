import os
import pathlib
from setuptools import setup
from importlib.machinery import SourceFileLoader

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# Version
version = (
    SourceFileLoader("dlops.version", os.path.join(
        "dlops", "version.py")).load_module().VERSION
)

setup(
    name="dlops",
    version=version,
    description="DLOps: Deep Learning Development for Production",
    long_description=README,
    long_description_content_type="text/markdown",
    url="http://dlops.io",
    project_urls={
        "Source Code": "https://github.com/dlops-io/dlops",
    },
    author="DLOps",
    author_email="info@dlops.io",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["dlops"],
    include_package_data=True,
    install_requires=[],
    entry_points={
    },
)
