import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("CAN Visualizer")

#Buttons on top
topFrame = tk.Frame(root)
topFrame.pack()
visButton = tk.Button(topFrame,text="Can Bus Visualizer",padx=50)
visButton.pack(side="left")
visButton2 = tk.Button(topFrame,text="Nodes",padx=50)
visButton2.pack(side="right")
visButton3 = tk.Button(topFrame,text="Visualizer",padx=50)
visButton3.pack(side="left")
visButton4 = tk.Button(topFrame,text="Packets",padx=50)
visButton4.pack(side="right")

#PacketList
packetListFrame = ttk.LabelFrame(root)
packetListFrame.pack()
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

#PacketDetail Frame
packetDetailFrame = ttk.Treeview(root)
packetDetailFrame.pack()

#Ethernet II
eth = packetDetailFrame.insert('',0,text="Ethernet II, Src: ")

#Internet Protocol
ipv = packetDetailFrame.insert('',1,text="Internet Protocol Version 4, Src: ")

#User Datagram
udp = packetDetailFrame.insert('',2,text="User Datagram Protocol, Src Port: ")

#Domain Name
dns = packetDetailFrame.insert('','end',text="Domain Name System (response)" )
packetDetailFrame.insert(dns,0,text="time")

#Packet Bytes Frame
packetByteFrame =ttk.Treeview(root)
packetByteFrame.pack(expand=True, fill="both")

colnames2 = ttk.Treeview(packetByteFrame)
colnames2["columns"] = ("C1", "C2", "C3")
colnames2.column("#0", width=100, minwidth=200, stretch=tk.NO)
colnames2.column("C1", width=150, minwidth=200, stretch=tk.NO)
colnames2.column("C2", width=150, minwidth=200, stretch=tk.NO)
colnames2.column("C3", width=150, minwidth=200, stretch=tk.NO)

colnames2.heading("#0", text="TimeStamp", anchor=tk.W)
colnames2.heading("C1", text="CanBus Type", anchor=tk.W)
colnames2.heading("C2", text="ID", anchor=tk.W)
colnames2.heading("C3", text="Data", anchor=tk.W)

root.mainloop()