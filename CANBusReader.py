import os
import threading
import subprocess
import sys


# Command to read packets from CAN bus
subprocess.Popen(['candump -L vcan0 > CapturedPackets.pcap'], shell=True) # Create background process to run shell command
user_input = input('Type STOP to end live capture: ')
if user_input.upper() == 'stop':
    sys.exit(1)


