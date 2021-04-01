
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




def viewEntry():
    global mycursor
    root=t.ThemedTk(theme="radiance")
    root.title("View Data Section")
    root.geometry("1150x600")
    root.wm_iconbitmap(r"res/viewlogo.ico")
    root.config(bg="#2C3335")
    Canvas1 = Canvas(root)

    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)

    Canvas1.config(bg="#2C3335")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="View Details",
                         bg='black', fg='white', font=("hack 20"))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Canvas(root,bg='black',yscrollcommand = scrollbar.set)
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.55)
    y = 0.25

    scrollbar.config(command=labelFrame.yview)



    mylabel=Label(labelFrame,text="%-20s%-32s%-30s%-40s%-50s" % ('RollNo', 'Name',
                                                     'Class', 'Phone No.',"Address"), bg='black', fg='white').place(relx=0.07, rely=0.1)
    Label(labelFrame, text="---------------------------------------------------------------------------------------------------------------------------------------------------------------------",
          bg='black', fg='white').place(relx=0.05, rely=0.2)
    


    Com=("SELECT * FROM student")
    try:
        mycursor.execute(Com)
        myresult = mycursor.fetchall()
        for i in myresult:
            Label(labelFrame, text="%-20s%-32s%-30s%-40s%-50s" %
                  (i[0], i[1], i[2], i[3],i[4]), bg='black', fg='white').place(relx=0.07, rely=y)
            y += 0.1
    except:
        tmsg.showerror("ERROR 404","Something Went Wrong\nUnable To Fetch Data,Try Again")

    s = ttk.Style().configure('my.TButton', font="hack 17")

    ttk.Button(root, text="Exit", style="my.TButton",
               command=root.destroy, width=15).place(relx=0.4, rely=0.89)

    root.mainloop()
