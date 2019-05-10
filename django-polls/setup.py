import os
from setuptools import find_pachkages, setup

with open(os.path.join.dirname(__file__), 'README.rst') as readme;
	README = readme.read()
	
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
	name='django-polls',
	version='0.1',
	packages=find_pachkages(),
	include_package_data=True
	license='BSD License',
	description='A simple Django app to conduct Web-based polls.',
	long_description=README,
	url='https://www.example.com/',
	author='Your Name',
	author_email='yourname@example.com',
	classifiers=[
		'Environment :: Web Environment',
		'Framework :: Django',
		'Framework :: Django :: X.Y',
		'Intended Audience :: Developers',
	]
)