#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import versioneer

setup(
    name="versio9",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="VersionOne API client",
    author="doubleO8",
    author_email="wb008@hdm-stuttgart.de",
    license="MIT/BSD",
    keywords="versionone v1 api sdk",
    url="https://github.com/doubleO8/versionone-sdk-spoon",
    # https://github.com/{username}/{module_name}/tarball/{tag}.
    download_url="https://github.com/doubleO8/versionone-sdk-spoon/tarball/0.5.0",
    packages=[
        'versio9',
    ],
    test_suite="versio9.tests",
)
