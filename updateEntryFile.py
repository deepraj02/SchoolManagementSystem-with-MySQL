

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


def clear1():
    roll.delete(0, END)
    nam.delete(0, END)
    clas.delete(0, END)
    phon.delete(0, END)
    addr.delete(0, END)


def updateThatName():
    global mycursor, roll, nam
    sql = "UPDATE Student SET Name =(%s) WHERE RollNo = %s"
    valls=(nam.get(),roll.get())
    mycursor.execute(sql,valls)
    mydb.commit()
    tmsg.showinfo("INFO", "Data Updated Successfully\n")
    clear1()


def updateThatClass():
    global mycursor, clas, roll
    sql = f"UPDATE Student SET Class = {clas.get()} WHERE RollNo = {roll.get()}"
    mycursor.execute(sql)
    mydb.commit()
    tmsg.showinfo("INFO", "Data Updated Successfully\n")
    clear1()

def updateThatPhone():
    global mycursor, phon, roll
    sql = f"UPDATE Student SET Phone = {phon.get()} WHERE RollNo = {roll.get()}"
    mycursor.execute(sql)
    mydb.commit()
    tmsg.showinfo("INFO", "Data Updated Successfully\n")
    clear1()

def updateThatAddress():
    global mycursor, addr, roll
    sql = "UPDATE Student SET Address = %s WHERE RollNo = %s"
    vall=(addr.get(),roll.get())
    mycursor.execute(sql,vall)
    mydb.commit()
    tmsg.showinfo("INFO", "Data Updated Successfully\n")
    clear1()

def updateThatSucker():
    global mycursor, roll, nam, clas, phon, addr
    sql = "UPDATE Student SET Name = %s, Class= %s, Phone= %s, Address= %s WHERE RollNo = %s"
    val=(nam.get(),clas.get(),phon.get(),addr.get(),roll.get())
    mycursor.execute(sql,val)
    mydb.commit()
    tmsg.showinfo("INFO", "Data Updated Successfully\n")
    clear1()

roll = ""
nam = ""
clas = ""
phon = ""
addr = ""


def updateEntry():
    global roll, nam, clas, phon, addr
    root = t.ThemedTk(theme="adapta")
    root.title("Data Update Portal")
    root.wm_iconbitmap(r"res/update.ico")
    root.geometry("750x600")
    root.config(bg="#2C3335")
    Canvas1 = Canvas(root)

    Canvas1.config(bg="#2C3335")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Update Entry",
                         bg='black', fg='white', font=("hack 20"))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
    lb2 = Label(labelFrame, text="Roll NO : ", bg='black',
                fg='white', font="hack 14")
    lb2.place(relx=0.08, rely=0.2)
    lb2 = Label(labelFrame, text="Name : ", bg='black',
                fg='white', font="hack 14")
    lb2.place(relx=0.08, rely=0.3)
    lb2 = Label(labelFrame, text="Class : ", bg='black',
                fg='white', font="hack 14")
    lb2.place(relx=0.08, rely=0.4)
    lb2 = Label(labelFrame, text="Phone No.",
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

    s = ttk.Style().configure('my.TButton', font="hack 11")

    ttk.Button(root, text="U.Name", style="my.TButton",
               command=updateThatName, width=6).place(relx=0.06, rely=0.87)
    ttk.Button(root, text="U.Class", style="my.TButton",
               command=updateThatClass, width=6).place(relx=0.179, rely=0.87)
    ttk.Button(root, text="U.PhoneNo.", style="my.TButton",
               command=updateThatPhone, width=6).place(relx=0.299, rely=0.87)
    ttk.Button(root, text="U.Addr", style="my.TButton",
               command=updateThatAddress, width=6).place(relx=0.419, rely=0.87)
    ttk.Button(root, text="U.All", style="my.TButton",
               command=updateThatSucker, width=6).place(relx=0.535, rely=0.87)
    ttk.Button(root, text="Clear", style="my.TButton",
               command=clear1, width=6).place(relx=0.755, rely=0.87)
    ttk.Button(root, text="Exit", style="my.TButton",
               command=root.destroy, width=6).place(relx=0.869, rely=0.87)

    root.mainloop()
