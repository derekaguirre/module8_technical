# This file is used to build the GUI of the CAN Bus visualizer
from tkinter import *


def print_hello():
    print('Hello')

root = Tk()
root.title('CAN Bus Visualizer')
root.geometry('400x300') # Set window size

play_button = Button(root, text='Play', padx=40, pady=20, command=print_hello)


root.mainloop() # Keep running app
