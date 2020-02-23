# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in nyumbafix/__init__.py
from nyumbafix import __version__ as version

setup(
	name='nyumbafix',
	version=version,
	description='Work sharing app',
	author='Proenterprise, Nyumbafix and Collaborators',
	author_email='hello@erp.co.zm',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
