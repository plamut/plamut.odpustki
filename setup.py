# -*- coding: utf-8 -*-
"""Installer for the plamut.odpustki package."""

from setuptools import setup

setup(
    name='Odpustki',
    version='0.1',

    # list of packages to process during setup
    packages=['plamut.odpustki'],

    # keys: package names (empty name stands for root package)
    # values: directory names relative to distribution root where packages
    #         (denoted by <key>) reside
    # ---> meaning: "all packages (=empty string) reside in the src dir"
    package_dir = {'': 'src'},
    include_package_data=True,

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=[
        #'docutils>=0.3',
        'Plone',
        'setuptools',
    ],

    # metadata for upload to PyPI
    author='Peter Lamut',
    author_email='peter.lamut@niteoweb.com',
    description='This is a plamut.odpustki package',
    license='BSD',
    keywords='example odpustki',

    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
