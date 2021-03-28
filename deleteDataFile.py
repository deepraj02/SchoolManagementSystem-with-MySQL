from tkinter import *
import mysql.connector
import tkinter.messagebox as tmsg
import pyfiglet
from ttkthemes import themed_tk as t
from tkinter import ttk


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="deepraj02",
    database="schoolmanagement"
)

mycursor = mydb.cursor()


def deleteThatSucker():
    global mycursor, roo

    # a = input("Enter Your Rollno:\t")
    # b = input("Enter Your Name:\t")
    # c = input("Enter your Class:\t")
    # d = input("Enter Your Phone Number:\t")
    # e = input("Enter your Address:\t\n")


    sql = f"DELETE FROM Student WHERE rollno = {roo.get()}"
    mycursor.execute(sql)
    mydb.commit()
    tmsg.showinfo("INFO", "Data Removed Successfully\n")
    ClearInput()


roo = ""
nam = ""
clas = ""
phon = ""
addr = ""


def ClearInput():
    roo.delete(0, END)



def deleteEntry():
    global roo, nam, clas, phon, addr
    root = t.ThemedTk(theme="radiance")
    root.title("Data Remove Portal")
    root.wm_iconbitmap(r"res/remm.ico")
    root.geometry("750x600")
    root.config(bg="#2C3335")
    Canvas1 = Canvas(root)

    Canvas1.config(bg="#2C3335")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Delete Entry",
                         bg='black', fg='white', font=("hack 20"))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Book ID to Delete
    lb2 = Label(labelFrame, text="Roll N0. : ",
                bg='black', fg='white', font="hack 15")
    lb2.place(relx=0.05, rely=0.5)


    roo = Entry(labelFrame, width=8, font="firacode 17")
    roo.place(relx=0.3, rely=0.5, relwidth=0.62)

    s = ttk.Style().configure('my.TButton', font="firacode 15")
    ttk.Button(root, text="Enter", style="my.TButton",
               command=deleteThatSucker, width=15).place(relx=0.055, rely=0.87)
    ttk.Button(root, text="Clear", style="my.TButton",
               command=ClearInput, width=15).place(relx=0.36, rely=0.87)
    ttk.Button(root, text="Exit", style="my.TButton",
               command=root.destroy, width=15).place(relx=0.676, rely=0.87)
    root.mainloop()

# deleteEntry()