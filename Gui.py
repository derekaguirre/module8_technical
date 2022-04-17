from textwrap import fill
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('CAN Visualizer')
root.geometry('{}x{}'.format(750, 875))

# create all of the main containers
topButtonframe = tk.Frame(root)
settingsFrame = tk.Frame(root)
packetListFrame = ttk.Frame(root)
packetDetailView = ttk.Treeview(root)
packetByteView =ttk.Treeview(root)

# layout all of the main containers
topButtonframe.grid(sticky="n")
settingsFrame.grid(sticky="n")
packetListFrame.grid(sticky="new")
packetDetailView.grid(sticky="new")
packetByteView.grid(sticky="new")

# create the button for the top button frame
visButton = tk.Button(topButtonframe,text="Can Bus Visualizer",padx=50)
visButton2 = tk.Button(topButtonframe,text="Nodes",padx=50)
visButton3 = tk.Button(topButtonframe,text="Visualizer",padx=50)
visButton4 = tk.Button(topButtonframe,text="Packets",padx=50)
visButton5 = tk.Button(topButtonframe,text="ER",padx=30)

# layout the button in the top frame
visButton.grid(row=0, column=1)
visButton2.grid(row=0, column=2)
visButton3.grid(row=0, column=3)
visButton4.grid(row=0, column=4)
visButton5.grid(row=0, column=5)

# create buttons for the setting frame
fileButton = tk.Button(settingsFrame,text="File",padx=10)
editButton = tk.Button(settingsFrame,text="Edit",padx=10)
viewButton = tk.Button(settingsFrame,text="View",padx=10)
settingsButton = tk.Button(settingsFrame,text="Settings",padx=10)
helpButton = tk.Button(settingsFrame,text="Help",padx=10)
zoomButton = tk.Button(settingsFrame,text="Zoom",padx=10)
playButton = tk.Button(settingsFrame,text="Play",padx=10)
stopButton = tk.Button(settingsFrame,text="Stop",padx=10)

# layout the button in the settings frame
fileButton.grid(row=1, column=1)
editButton.grid(row=1, column=2)
viewButton.grid(row=1, column=3)
settingsButton.grid(row=1, column=4)
helpButton.grid(row=1, column=5)
zoomButton.grid(row=1, column=6)
playButton.grid(row=1, column=7)
stopButton.grid(row=1, column=8)

#PacketList
colnames1 = ttk.Treeview(packetListFrame)
colnames1["columns"] = ("C1", "C2", "C3")
colnames1.column("#0", width=100, minwidth=200, stretch=tk.NO)
colnames1.column("C1", width=150, minwidth=200, stretch=tk.NO)
colnames1.column("C2", width=150, minwidth=200, stretch=tk.NO)
colnames1.column("C3", width=150, minwidth=200, stretch=tk.NO)

colnames1.heading("#0", text="TimeStamp", anchor=tk.W)
colnames1.heading("C1", text="CanBus Type", anchor=tk.W)
colnames1.heading("C2", text="ID", anchor=tk.W)
colnames1.heading("C3", text="Data", anchor=tk.W)

#Populate PacketList
t = {}
for i in range(5):
    t[i] = colnames1.insert("", i, text="Example " + str(i), values=("val1", "val2"))
colnames1.pack(expand=True, fill="both")

#Populate PacketDetail
#Ethernet II
eth = packetDetailView.insert('',0,text="Ethernet II, Src: ")

#Internet Protocol
ipv = packetDetailView.insert('',1,text="Internet Protocol Version 4, Src: ")

#User Datagram
udp = packetDetailView.insert('',2,text="User Datagram Protocol, Src Port: ")

#Domain Name
dns = packetDetailView.insert('','end',text="Domain Name System (response)" )
packetDetailView.insert(dns,0,text="time")

#Packet Bytes Frame
colnames1 = ttk.Treeview(packetByteView)
colnames1["columns"] = ("C1", "C2", "C3")
colnames1.column("#0", width=100, minwidth=200, stretch=tk.NO)
colnames1.column("C1", width=150, minwidth=200, stretch=tk.NO)
colnames1.column("C2", width=150, minwidth=200, stretch=tk.NO)
colnames1.column("C3", width=150, minwidth=200, stretch=tk.NO)

colnames1.heading("#0", text="TimeStamp", anchor=tk.W)
colnames1.heading("C1", text="CanBus Type", anchor=tk.W)
colnames1.heading("C2", text="ID", anchor=tk.W)
colnames1.heading("C3", text="Data", anchor=tk.W)

root.mainloop()