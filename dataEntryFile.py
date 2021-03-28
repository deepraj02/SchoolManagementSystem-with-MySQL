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


def Values():
    global mycursor, roll
    # a = input("Enter Your Rollno:\t")
    # b = input("Enter Your Name:\t")
    # c = input("Enter your Class:\t")
    # d = input("Enter Your Phone Number:\t")
    # e = input("Enter your Address:\t\n")

    sql = "INSERT INTO student VALUES (%s, %s, %s, %s, %s)"

    val = (roll.get(), nam.get(), clas.get(), phon.get(), addr.get())
    mycursor.execute(sql, val)
    mydb.commit()
    tmsg.showinfo("INFO", "Data Entered Successfully\n")
    ClearInput()


roll = ""
nam = ""
clas = ""
phon = ""
addr = ""


def ClearInput():
    roll.delete(0, END)
    nam.delete(0, END)
    clas.delete(0, END)
    phon.delete(0, END)
    addr.delete(0, END)


def dataEntry():
    global roll, nam, clas, phon, addr
    root = t.ThemedTk(theme="breeze")
    root.title("Data Entry Portal")
    root.wm_iconbitmap(r"res/dataent.ico")
    root.geometry("750x600")
    root.config(bg="#2C3335")
    Canvas1 = Canvas(root)

    Canvas1.config(bg="#2C3335")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Enter Details Here",
                         bg='#2C3335', fg='#FCBBF8', font=('hack 20'))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Book ID to Delete
    lb2 = Label(labelFrame, text="Roll NO : ", bg='black',
                fg='white', font="hack 14")
    lb2.place(relx=0.08, rely=0.2)
    lb2 = Label(labelFrame, text="Name : ", bg='black',
                fg='white', font="hack 14")
    lb2.place(relx=0.08, rely=0.3)
    lb2 = Label(labelFrame, text="Class : ", bg='black',
                fg='white', font="hack 14")
    lb2.place(relx=0.08, rely=0.4)
    lb2 = Label(labelFrame, text="Phone No. : ",
                bg='black', fg='white', font="hack 14")
    lb2.place(relx=0.08, rely=0.5)
    lb2 = Label(labelFrame, text="Address : ", bg='black',
                fg='white', font="hack 14")
    lb2.place(relx=0.08, rely=0.6)

    roll = Entry(labelFrame, width=8, font="hack 17")
    roll.place(relx=0.28, rely=0.2, relwidth=0.62)

    nam = Entry(labelFrame, width=8, font="hack 17")
    nam.place(relx=0.28, rely=0.3, relwidth=0.62)
    clas = Entry(labelFrame, width=8, font="hack 17")
    clas.place(relx=0.28, rely=0.4, relwidth=0.62)
    phon = Entry(labelFrame, width=8, font="hack 17")
    phon.place(relx=0.28, rely=0.5, relwidth=0.62)
    addr = Entry(labelFrame, width=8, font="hack 17")
    addr.place(relx=0.28, rely=0.6, relwidth=0.62)

    # Submit Button
    s = ttk.Style().configure('my.TButton', font="hack 16")

    ttk.Button(root, text="Enter", style="my.TButton",
               command=Values, width=15).place(relx=0.055, rely=0.87)
    ttk.Button(root, text="Clear", style="my.TButton",
               command=ClearInput, width=15).place(relx=0.36, rely=0.87)
    ttk.Button(root, text="Exit", style="my.TButton",
               command=root.destroy, width=15).place(relx=0.676, rely=0.87)
    root.mainloop()


