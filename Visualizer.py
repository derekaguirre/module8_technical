import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
import sys


class StdoutRedirectorLabel(object):

    def __init__(self, widget):
        self.widget = widget
        # clear at start because it will use +=
        self.widget['text'] = ''

    def write(self, text):
        # have to use += because one `print()` executes `sys.stdout` many times
        self.widget['text'] += text


def callback1():
    import test

    # keep original `sys.stdout
    old_stdout = sys.stdout

    # redirect to class which will add text to `lbl`
    sys.stdout = StdoutRedirectorLabel(lbl)

    # it will execute only `function3` and assign result to Label (with ending "\n")
    test.function1()

    # set back original `sys.stdout
    sys.stdout = old_stdout


# --- main ---
root = tk.Tk()
root.title('CAN Bus Visualizer - Decode Packets')
root.geometry("800x500")
lbl = tk.Label(root, text='')
lbl.pack()

my_menu = tk.Menu(root)
root.config(menu=my_menu)


def our_command():
    tk.Label(root, text="Needs implementation").pack()


def file_new():
    file_new_frame.grid(row=0, column=0)
    file_new_frame.pack(fill="both", expand=1)


def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=(('mdf files', '*.mf4'),))
    tk.Label(root, text=filename).pack()


# Create a menu item
file_menu = tk.Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open...", command=select_file)
file_menu.add_separator()
file_menu.add_command(label="Save As...", command=our_command)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Create a decode menu item
packets_menu = tk.Menu(my_menu)
my_menu.add_cascade(label="Packets", menu=packets_menu)
packets_menu.add_command(label="Decode", command=callback1)

# Frame 1
file_new_frame = tk.Frame(root, width=800, height=500, bg="gray")

root.mainloop()
