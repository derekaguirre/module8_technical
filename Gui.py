import tkinter as tk
from tkinter import ttk

headings = ["Heading0", "Heading1", "Heading2", "Heading3"]

root = tk.Tk()
root.title("CAN Visualizer")

frame1 = tk.Frame(root)
frame1.pack()
tree = ttk.Treeview(frame1)
tree["columns"] = ("C1", "C2", "C3")
tree.column("#0", width=100, minwidth=200, stretch=tk.NO)
tree.column("C1", width=150, minwidth=200, stretch=tk.NO)
tree.column("C2", width=150, minwidth=200, stretch=tk.NO)
tree.column("C3", width=150, minwidth=200, stretch=tk.NO)

tree.heading("#0", text="TimeStamp", anchor=tk.W)
tree.heading("C1", text="CanBus Type", anchor=tk.W)
tree.heading("C2", text="ID", anchor=tk.W)
tree.heading("C3", text="Data", anchor=tk.W)

t = {}

for i in range(5):
    t[i] = tree.insert("", i, text="Example " + str(i), values=("val1", "val2"))
tree.pack(expand=True, fill="both")

def create():
    for i, val in enumerate(headings):
        if i == 0:
            tree2.column("#0", width=200, minwidth=200, stretch=tk.NO)
        elif i == 1:
            tree2["columns"] = ("C1", )
            tree2.column("C1", width=800, minwidth=200, stretch=tk.NO)
        else:
            tree2["columns"] = tree2["columns"] + ("C" + str(i), )
            tree2.column("C" + str(i), width=800, minwidth=200, stretch=tk.NO)

    for i, val in enumerate(headings):
        if i == 0:
            tree2.heading("#0", text=val, anchor=tk.W)
        elif i == 1:
            tree2.heading("C1", text=val, anchor=tk.W)
        else:
            tree2.heading("C" + str(i), text=val, anchor=tk.W)


btn1 = tk.Button(frame1, text="Add", command=create)
btn1.pack(side="top")

tree2 = ttk.Treeview(frame1)


tree2.pack(expand=True, fill="both")

root.mainloop()