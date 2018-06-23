# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='block_viewer',
    version='1.0.0',
    description='a viewer for bitcoin block structure including blockheaer, transactions etc.',
    long_description=readme,
    author='Yan Qian',
    author_email='qianyan.lambda@gmail.com',
    url='https://github.com/qianyan/bitcoin-viewer',
    license=license,
    packages=find_packages('src', exclude=('tests', 'docs')),
    package_dir={'': 'src'},
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    entry_points = {
        'console_scripts': [
            'block_viewer=block_viewer.cli:main',
        ],
    },
    install_requires=[
        'requests',
        'python-bitcoinlib==0.5.0'
    ]
)

