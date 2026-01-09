"""Setup configuration for noveum-sdk-python.

This file provides setuptools compatibility alongside Poetry.
Most configuration is in pyproject.toml.
"""

from setuptools import find_packages, setup

setup(
    name="noveum-sdk-python",
    packages=find_packages(),
    package_data={"noveum_api_client": ["py.typed"]},
    python_requires=">=3.10",
)
