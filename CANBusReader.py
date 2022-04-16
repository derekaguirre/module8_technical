import os
import threading
import subprocess
import sys


# Command to read packets from CAN bus
subprocess.Popen(['candump -u -L vcan0 > CapturedPackets.pcap'], shell=True) # Create background process to run shell command

# Exit command
user_input = input('Type STOP to end live capture: ')
if user_input.upper() == 'STOP':
    sys.exit(1)


