#!/usr/bin/env python2.7
import sys
from setuptools import setup, find_packages

install_requires = [
    "django",
    "jinja2",
    "werkzeug",
    "twilio",
]

tests_require = [
    'coverage',
    'mock',
    'ngrok',
]

setup_requires = [
    'nose',
]


setup(
    name='hassleapps',
    git_version=True,
    description='Apps against Facebook',
    zip_safe=False,
    package_dir={'':'src/main/python'},
    packages=find_packages('src/main/python'),
    setup_requires=setup_requires,
    tests_require=tests_require,
    install_requires=install_requires,
)
