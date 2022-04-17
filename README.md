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