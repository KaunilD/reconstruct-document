
import re
import os
from setuptools import setup


version = '1.0.0'

description = ''
with open('README.md', 'rb') as file:
    description = file.read().decode('utf-8')

setup(name='reconstruct_document',
    version=version,
    description='Command line document reconstruction utility.',
    long_description=description,
    entry_points = {
        'console_scripts': ['reconstruct_document = reconstruct_document.reconstruct_document:main']
    },
    url='http://kaunild.github.io',
    author='Kaunil Dhruv',
    author_email='dhruv.kaunil@gmail.com',
    license='BSD',
    packages=['reconstruct_document', 'test']
)
