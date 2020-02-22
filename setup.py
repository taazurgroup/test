# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in test2/__init__.py
from test2 import __version__ as version

setup(
	name='test2',
	version=version,
	description='Test2',
	author='MIT',
	author_email='santosh.baburao@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
