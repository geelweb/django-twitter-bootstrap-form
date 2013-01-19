#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# License: MIT
# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4:

"""
django twitter bootstrap form setup script
"""

__author__ = "Guillaume Luchet <guillaume@geelweb.org>"
__version__ = "0.1"

import sys
from setuptools import setup, find_packages

author_data = __author__.split(" ")
maintainer = " ".join(author_data[0:-1])
maintainer_email = author_data[-1]
long_desc = open('README.md').read()

if __name__ == "__main__":
    setup(
        name="django twitter bootstrap form",
        version=__version__,
        description="Render Django forms as described using the twitter bootstrap HTML layout",
        long_description=long_desc,
        author=maintainer,
        author_email=maintainer_email,
        maintainer=maintainer,
        maintainer_email=maintainer_email,
        url="https://github.com/geelweb/django-twitter-bootstrap-form",
        license='MIT',
        namespace_packages = ['geelweb', 'geelweb.django'],
        packages=find_packages('src'),
        package_dir = {'':'src'},
        package_data = {
            'geelweb.django.twitter_bootstrap_form': [
                'templates/twitter_bootstrap_form/*.html',
                ],
        },
        zip_safe=False
        )

