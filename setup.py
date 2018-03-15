#!/usr/bin/env python3

from setuptools import setup

setup(
    name="usconstitution",
    version="1.0",
    description="Read the US Constitution right from your terminal",
    long_description=open("README.md").read(),
    license="MIT",
    packages=["libusconstitution"],
    scripts=["usconstitution"],
    package_data={"libusconstitution": ["data/*"]},
)
