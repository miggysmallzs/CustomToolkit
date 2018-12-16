#!/usr/bin/python
#
# The purpose of this script is to automate checking PTR records for entire IP blocks.
# Usage: ./ptr-scan.py {IP Block such as 192.168.0.0/24}
#
#
#
import os
import sys
import subprocess
from sys import argv
import re


# Default Variables
iplist = []
counter = 0
BLOCK = ''

# Function for creating the list of IP's to check, uses the CIDR block you supply as an argument to the script
def GOLDDIGGER ( BLOCK ):
        callp1 = subprocess.Popen(['prips', BLOCK], stdout=subprocess.PIPE)
        outputp1 = callp1.stdout.read()
        iplist = outputp1.split()

        for IP in iplist:
                callp2 =subprocess.Popen(
                                ['dig', '-x', IP],
                                stdout=subprocess.PIPE)
                callp3 = subprocess.Popen(
                                ['grep', 'PTR'],
                                stdin=callp2.stdout,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
                callp2.stdout.close() # Allow callp2 to receive a SIGPIPE if callp3 exits.

                FINAL = callp3.stdout.read()
                print '{QUERYING IP ADDRESS ----- ', IP, ' ----- }'
                print FINAL

def inputcheck()

# Execution of script PART 1
if len (sys.argv) == 2:
        BLOCK = sys.argv[1]
        GOLDDIGGER( BLOCK )