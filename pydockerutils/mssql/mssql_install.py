"""
pydockerutils
-------------------------------
 - Eugenio Marinetto
 - nenetto@gmail.com
-------------------------------
Created 14-05-2018
"""

from pydockerutils.prettymessaging import printer as pm
import subprocess
import sys


def install():

    # Check platform
    if sys.platform.startswith('linux'):
        pm.print_info('Installing MSSQL Drivers')

        commands = ['apt-get update',
                    'DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends apt-utils',
                    'DEBIAN_FRONTEND=noninteractive apt-get -y install apt-transport-https curl',
                    'curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -',
                    'curl https://packages.microsoft.com/config/debian/8/prod.list > /etc/apt/sources.list.d/mssql-release.list',
                    'echo "deb http://security.debian.org/debian-security jessie/updates main" >> /etc/apt/sources.list',
                    'apt-get update',
                    'DEBIAN_FRONTEND=noninteractive ACCEPT_EULA=Y apt-get -y install msodbcsql',
                    'DEBIAN_FRONTEND=noninteractive ACCEPT_EULA=Y apt-get -y install mssql-tools',
                    'DEBIAN_FRONTEND=noninteractive apt-get -y install unixodbc-dev',
                    'DEBIAN_FRONTEND=noninteractive apt-get install libssl1.0.0',
                    'DEBIAN_FRONTEND=noninteractive apt-get -y install python-pyodbc',
                    'DEBIAN_FRONTEND=noninteractive apt-get -y install locales',
                    'echo "en_US.UTF-8 UTF-8" > /etc/locale.gen',
                    'locale-gen',
                    'rm -rf /var/lib/apt/lists/*'
                    ]

        for c in commands:
            pm.print_info('[{0}]'.format(c), padding=2)
            session = subprocess.Popen(c, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            stdout, stderr = session.communicate()
            session.wait()

            output_lines = stdout.decode("utf-8").split('\n')
            for ol in output_lines:
                pm.print_info_2(ol, padding=3)

            if session.returncode != 0:
                e = stderr.decode("utf-8")
                pm.print_error('Installation failed!')
                pm.print_info_2('Error: {0}'.format(str(e)))
                pm.print_error('Exit', exit_code=0)

            else:
                e = stderr.decode("utf-8").split('\n')
                for ee in e:
                    pm.print_info(ee, padding=4)


    elif sys.platform.startswith('darwin'):

        pm.print_info('Checking installation', padding=2)
        session = subprocess.Popen('brew list', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdout, stderr = session.communicate()
        session.wait()

        installed = stdout.decode("utf-8").split('\n')

        if 'msodbcsql@13.1.9.2' in installed and 'mssql-tools@14.0.6.0' in installed:
            pm.print_info('Your installation seems to be correct')
        else:
            pm.print_warning('Your installation seems to be incorrect')

            commands = ['/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"',
                        'brew tap microsoft/mssql-release https://github.com/Microsoft/homebrew-mssql-release',
                        'brew update',
                        'brew install --no-sandbox msodbcsql@13.1.9.2 mssql-tools@14.0.6.0']

            pm.print_warning('Make sure you have installed MSSQL Drivers following the instructions bellow')
            pm.print_separator()
            for c in commands:
                print(c)
            pm.print_separator()

    elif sys.platform.startswith('win'):
        pm.print_warning('Currently, pymake for MSSQL connections is not supported')
