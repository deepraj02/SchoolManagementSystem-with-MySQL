from tkinter import *
import mysql.connector
import tkinter.messagebox as tmsg
import pyfiglet
from ttkthemes import themed_tk as t
from tkinter import ttk

def updateEntry():
    root=t.ThemedTk(theme="radiance")
    root.title("KV Kailashahar Portal")
    root.geometry("750x600")

    root.configure(background='#2C3335')

    root.mainloop()