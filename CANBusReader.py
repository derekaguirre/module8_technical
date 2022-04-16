import os
import subprocess
import signal


# Read packets from CAN Bus and save them into Captured and Decoded files
class CANBusReader:
    def __init__(self, dbc_file):
        self.dbc_file = dbc_file

        # Init process variables
        self.can_sniff = None
        self.can_gen = None
        self.can_decode = None


    # Command to read packets Live from CAN bus
    # Used when user toggles/enables live feed.
    def start_live_feed(self):
        # Generate/open file to store packets
        cp_file = open('CapturedPackets.pcap', 'w') 
        dec_file = open('DecodedPackets.pcap', 'w')
        self.can_sniff = subprocess.Popen(['cansniffer vcan0'], shell=True, stdout=cp_file, preexec_fn=os.setsid) # Create sniffing process
        self.can_gen = subprocess.Popen(['cangen vcan0'], shell=True, preexec_fn=os.setsid) # Create CAN generating process
        self.can_decode = subprocess.Popen([f'candump vcan0 | python3 -m cantools decode {self.dbc_file}'], shell=True, stdout=dec_file, preexec_fn=os.setsid) # Create background decoding process


    # Kill existing running processes used to fetch and decode live feed
    # This method is only callend after start_live_feed has been called
    def stop_live_feed(self):
        os.killpg(os.getpgid(self.can_sniff.pid), signal.SIGKILL)  # Send signal to processes currently running
        os.killpg(os.getpgid(self.can_gen.pid), signal.SIGTERM)  
        os.killpg(os.getpgid(self.can_decode.pid), signal.SIGTERM)  

