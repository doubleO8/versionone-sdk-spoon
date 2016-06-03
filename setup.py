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
    author="Joe Koberg (VersionOne, Inc.)",
    author_email="Joe.Koberg@versionone.com",
    license="MIT/BSD",
    keywords="versionone v1 api sdk",
    url="http://github.com/VersionOne/versio9",

    packages=[
        'versio9',
    ],

    install_requires=[
        # 'elementtree',
        # 'testtools',
        # 'iso8601',
        # 'python-ntlm',
    ],

    test_suite="versio9.tests",

)
