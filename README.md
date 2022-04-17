# module8_technical
This repo serves as a demonstration for a portion of functionality relating to the CAN Bus Visualizer tool currently in the design process.

* Note: `honda.dbc` is used as a test dbc file to decode the contents of the virtual can bus.

## Required set-Up
-------
In order to utilize this tool, you need to be running on a linux-based system.

### Step 1
`sudo apt-get install can-utils`
### Step 2
`pip install cantools`

## To Run
----
<i>Note: Current implementation runs on a virtual CAN Bus.</i>

### Step 1
Open a terminal and run the following commands in order:
```
$ sudo su
$ modprobe vcan
$ ip link add dev vcan0 type vcan
$ ip link set up vcan0
```
### Step 2
Check if the virtual CAN is running:

`ifconfig vcan0`

You should see the following or similar:

```
vcan0: flags=193<UP,RUNNING,NOARP>  mtu 72
        unspec 00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00  txqueuelen 1000  (UNSPEC)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

If CAN Bus network is not runnning, repeat from step 1 above.

### Step 3
Exit root mode:
- Ctrl + D

You may now run the program freely.

### Functionality covered
The functionality that the current version of the prototype covers is the reading and decoding 
of packets coming from the can bus network. The system proceeds to use three different processes 
to accomplish this task. In one sub-process, the system runs Can sniffer to read the packets 
coming from the Can Bus network. The second sub-process that the current process runs, it uses 
can_gen to generate packets. This sub-process Is used for testing only to simulate the connection 
to the Can Bus Network.  The third sub-process is in charge of decoding the packets captured in 
the first sub-process. The packets captured and the decoded packets are stored into two different 
files, CapturedPackets.pcap and DecodedPackets.pcap. The system then uses two threads to display 
packets into the user interface. One thread takes in the read packets and sends them to the 
interface. The second thread will then display the threads in the user’s interface.

### Status
The system only reads and decodes the packets. The system uses sub-processes to read and decode 
the packets. We seek to optimize it by using threads. There are buttons in the systems UI that 
are not functional for the moment.

### What did you learn?
 * After running the program for a while, the file storing the packet becomes pretty large. This 
could become a storage problem for sessions that are expected to take a long time.
 * A possible solution to the storage issue might be by using piping to avoid saving the packets.
 * Packages read from the network could produce storage problems.
 * Got a better understanding on reading and handling packets, along with a better understanding 
of packets structure