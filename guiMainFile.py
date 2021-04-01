from tkinter import *
import tkinter.messagebox as tmsg
import pyfiglet
import mysql.connector
from ttkthemes import themed_tk as t
from tkinter import ttk

from dataEntryFile import *
from deleteDataFile import *
from updateEntryFile import *
from viewDataFile import *
# & <--------------------- Functions --------------------->

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="deepraj02",
    database="schoolmanagement"
)

mycursor = mydb.cursor()


def exitME():
    k = tmsg.askquestion("Confirmation!", "Do You really want to **Exit**")
    if k == "yes":
        quit()


root = t.ThemedTk(theme="radiance")
root.title("KV Kailashahar Portal")


root.geometry("850x760")
root.minsize(850, 760)
a = pyfiglet.figlet_format("K.V\nKailashahar")
root.configure(background='#2C3335')
root.wm_iconbitmap(r"res/school.ico")


lb1 = Label(root, font='Hack 14', bg='#2C3335', fg='#D1E266')
lb1.pack(pady=30, ipady=10, ipadx=10, fill=BOTH)

lb2 = Label(root, font='Hack 17', bg='#2C3335', fg='#D1E266')
lb2.pack(pady=3, padx=6, ipady=5, ipadx=10, fill=BOTH)

lb1.configure(text=a)
lb2.configure(text="What Operation Would you like to Perform")

s = ttk.Style().configure('my.TButton', font="firacode 14")

ttk.Button(root, text="Enter Data", style="my.TButton",
           command=dataEntry, width=15).pack(padx=5, pady=10)
ttk.Button(root, text="View Data", style="my.TButton",
           command=viewEntry, width=15).pack(padx=5, pady=10)
ttk.Button(root, text="Update Data", style="my.TButton",
           command=updateEntry, width=15).pack(padx=5, pady=10)
ttk.Button(root, text="Delete Data", style="my.TButton",
           command=deleteEntry, width=15).pack(padx=5, pady=14)
ttk.Button(root, text="Quit Program", style="my.TButton",
           command=exitME, width=15).pack(padx=5)


root.mainloop()
