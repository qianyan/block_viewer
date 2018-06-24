# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='block_viewer',
    version='1.0.1',
    description='a viewer for bitcoin block structure including blockheaer, transactions etc.',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Yan Qian',
    author_email='qianyan.lambda@gmail.com',
    url='https://github.com/qianyan/block_viewer',
    license=license,
    packages=find_packages('src', exclude=('tests', 'docs')),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    package_dir={'': 'src'},
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    entry_points = {
        'console_scripts': [
            'block_viewer=block_viewer.cli:main',
        ],
    },
    install_requires=[
        'docopt==0.6.2',
        'requests',
        'python-bitcoinlib==0.5.0'
    ]
)

