#!/usr/bin/env python3

import os.path

from setuptools import setup

FILEPATH = os.path.dirname(os.path.abspath(__file__))
ABOUT_FILE_PATH = os.path.join(FILEPATH, 'radicale_dovecot_auth', '__about__.py')
ABOUT = {}
with open(ABOUT_FILE_PATH) as file_obj:
    exec(file_obj.read(), ABOUT)


setup(
        name='radicale_dovecot_auth',
        version=ABOUT['__version__'],
        description=ABOUT['__summary__'],
        url=ABOUT['__url__'],
        author=ABOUT['__author__'],
        author_email=ABOUT['__email__'],
        license=ABOUT['__license__'],
        packages=['radicale_dovecot_auth'],
        install_requires=['radicale'],
        classifiers=[
                'Development Status :: 5 - Production/Stable',
                'Operating System :: POSIX',
                'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
                'Programming Language :: Python :: 3',
                'Programming Language :: Python :: 3.3',
                'Programming Language :: Python :: 3.4',
                'Programming Language :: Python :: 3.5',
                'Programming Language :: Python :: 3.6',
                'Programming Language :: Python :: 3.7',
                'Programming Language :: Python :: 3.8'
                ]
        )
