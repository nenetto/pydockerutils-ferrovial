"""
pydockerutils
-------------------------------
 - Eugenio Marinetto
 - nenetto@gmail.com
-------------------------------
"""

from setuptools import setup, find_packages
from codecs import open
from os import path
import sys


here = path.abspath(path.dirname(__file__))

# PRE INSTALL COMMANDS COMES HERE
sys.path.append(here)


# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
        name='pydockerutils',
        version='1.0',
        description='Installers scripts for docker containers',
        long_description=long_description,
        url='https://github.com/nenetto/pydockerutils',
        author='Eugenio Marinetto',
        author_email='nenetto@gmail.com',
        packages=find_packages(exclude=("tests",)),
        install_requires=['setuptools>=39.1.0',
                          'tabulate>=0.8.2'],
        include_package_data=True,
        package_data={'': ['forticlient/files/linux/forticlient.sh',
                           'forticlient/files/linux/forticlient_setup',
                           'forticlient/files/linux/connect_vpn.sh'
                           ]
                      },
        entry_points={'console_scripts': ['install_forticlient = pydockerutils.forticlient.forticlient_install:install',
                                          'install_pyodbc = pydockerutils.mssql.mssql_install:install']}
        )
