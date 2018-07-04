"""
pydockerutils
-------------------------------
 - Eugenio Marinetto
 - nenetto@gmail.com
-------------------------------
Created 13-05-2018
"""

import sys
import subprocess
from pydockerutils.prettymessaging import printer as pm
import pkg_resources


def install():

    pm.print_info('Installing forticlient')

    # Check platform
    if sys.platform.startswith('linux'):
        pm.print_info_2('Platform: linux', padding=1)

        commands = ['apt-get update',
                    'DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends apt-utils',
                    'DEBIAN_FRONTEND=noninteractive apt-get -y install expect',
                    'DEBIAN_FRONTEND=noninteractive apt-get -y install ipppd',
                    'wget \'https://hadler.me/files/forticlient-sslvpn_4.4.2333-1_amd64.deb\' -O forticlient-sslvpn_amd64.deb',
                    'dpkg -x forticlient-sslvpn_amd64.deb /usr/share/forticlient',
                    pkg_resources.resource_filename('pydockerutils',
                                                    'forticlient/files/linux/forticlient_setup'),
                    'cp {0} /usr/bin/forticlient'.format(pkg_resources.resource_filename('pydockerutils',
                                                                                        'forticlient/files/linux/forticlient.sh')),
                    'cp {0} /usr/bin/connect_vpn'.format(pkg_resources.resource_filename('pydockerutils',
                                                                                        'forticlient/files/linux/connect_vpn.sh')),
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

    else:
        pm.print_warning('Platform: [{0}] is not supported! Sorry about that'.format(sys.platform))
        pm.print_error('Exiting', exit_code=1)
