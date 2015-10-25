#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# License: MIT
# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4:

"""
django twitter bootstrap form setup script
"""

__author__ = "Guillaume Luchet <guillaume@geelweb.org>"
__version__ = "0.4.0"

import os, sys
from setuptools import setup, find_packages

author_data = __author__.split(" ")
maintainer = " ".join(author_data[0:-1])
maintainer_email = author_data[-1]
README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

if __name__ == "__main__":
    setup(
        name="django-twitterbootstrap-form",
        version=__version__,
        description="Render Django forms as described using the twitter bootstrap HTML layout",
        long_description=README,
        author=maintainer,
        author_email=maintainer_email,
        maintainer=maintainer,
        maintainer_email=maintainer_email,
        url="https://github.com/geelweb/django-twitter-bootstrap-form",
        download_url="https://github.com/geelweb/django-twitter-bootstrap-form/tarball/0.3.3",
        license='MIT',
        namespace_packages = ['geelweb', 'geelweb.django'],
        packages=find_packages('src'),
        package_dir = {'':'src'},
        package_data = {
            'geelweb.django.twitter_bootstrap_form': [
                'templates/twitter_bootstrap_form/*.html',
                ],
        },
        keywords = ['django', 'twitter', 'bootstrap', 'form'],
        install_requires = [
            'django>=1.8',
            'django-widget-tweaks'
        ],
    )

