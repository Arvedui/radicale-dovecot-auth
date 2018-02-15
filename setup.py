#!/usr/bin/env python3

from setuptools import setup, find_packages

import radicale_dovecot_auth

setup(
    name='radicale_dovecot_auth',
    version=radicale_dovecot_auth.__version__,
    description="Dovecot authentication plugin for Radicale",
    url='https://github.com/Arvedui/radicale-dovecot-auth',
    author='Arvedui',
    author_email='arvedui@posteo.de',
    license="GNU GPL v3",
    packages=["radicale_dovecot_auth"],
    install_requires=['radicale'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Operating System :: POSIX',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
        ]
    )
