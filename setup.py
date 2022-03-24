"""
Setup the package.
"""
from setuptools import find_packages, setup

DESCRIPTION = 'Week day calculation.'
URL = 'https://github.com/andritar/week-day'

with open('README.md', 'r') as read_me:
    long_description = read_me.read()

with open('.project-version', 'r') as project_version_file:
    project_version = project_version_file.read().strip()


setup(
    version=project_version,
    name='week-day',
    author='andritar',
    author_email='tajasyck@gmail.com',
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=URL,
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.9',
    ],
)
