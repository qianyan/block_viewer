# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='bitcoin_viewer',
    version='0.1.0',
    description='a viewer for bitcoin structure including blockheaer, transactions etc.',
    long_description=readme,
    author='Yan Qian',
    author_email='qianyan.lambda@gmail.com',
    url='https://github.com/qianyan/bitcoin-viewer',
    license=license,
    packages=find_packages('src', exclude=('tests', 'docs')),
    package_dir={'': 'src'},
    setup_requires=['pytest-runner'],
    test_require=['pytest'],
    install_requires=[
        'python-bitcoinlib==0.5.0'
    ]
)

