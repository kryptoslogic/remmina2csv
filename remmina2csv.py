#!/usr/bin/env python

import sys
import csv

from glob import glob

if sys.version_info >= (3, 0):
    from configparser import ConfigParser
else:
    from ConfigParser import ConfigParser

#Write the CSV file to stdout with all fields in the first line
fields = ['postcommand','protocol','ssh_stricthostkeycheck','window_width','sshlogenabled','ssh_loopback','last_success','server','group','window_height','ssh_auth','ssh_proxycommand','ssh_ciphers','ssh_privatekey','ssh_server','sshlogname','ssh_kex_algorithms','exec','precommand','ssh_username','ssh_passphrase','ssh_charset','save_ssh_server','ssh_color_scheme','game','window_maximize','password','save_ssh_username','ssh_hostkeytypes','name','sshlogfolder','ssh_compression','disablepasswordstoring','ssh_password','viewmode','ssh_enabled']
out = csv.DictWriter(sys.stdout, fieldnames=fields)
out.writeheader()

for f in glob("*.remmina"):
    fo = open(f, 'r')
    ini = ConfigParser()
    ini.readfp(fo)

    protocol = None
    for sec in ini.sections():
        for key,value in ini.items(sec):
            if key == "protocol":
                protocol = value

    # Skip anything which isn't SSH, PRs are welcome to add support for the other protocol types
    if(protocol != "SSH"):
        continue

    #Write all rows
    for sec in ini.sections():
        row = {}
        for key,value in ini.items(sec):
            if key in fields:
                row[key] = value
        out.writerow(row)