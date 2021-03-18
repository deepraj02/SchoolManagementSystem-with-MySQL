
# ^ Importing The Modules

import pyfiglet
import mysql.connector

print(pyfiglet.figlet_format("WELCOME"))

# & Connecting to Database

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="deepraj02",
    database="schoolmanagement"
)

mycursor = mydb.cursor()

# * Function to add the Values to the Database


def enterValues():
    global mycursor
    a = input("Enter Your Rollno:\t")
    b = input("Enter Your Name:\t")
    c = input("Enter your Class:\t")
    d = input("Enter Your Phone Number:\t")
    e = input("Enter your Address:\t\n")

    sql = "INSERT INTO student VALUES (%s, %s, %s, %s, %s)"

    val = (a, b, c, d, e)
    mycursor.execute(sql, val)
    mydb.commit()
    print("Data Entered Successfully\n")


def showData():
    global mycursor
    mycursor.execute("SELECT * FROM student")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    print("Data Showed:-(Empty when there's no data)\n")


def clearData():
    global mycursor
    rol =input("Enter the Rollno of the Student you want to Delete:\t")
    sql = f"DELETE FROM Student WHERE rollno = {rol}"

    mycursor.execute(sql)

    mydb.commit()
    print("Data Removed Successfully:\n")


def updateData():
    global mycursor
    print("Which Field you want to update:\t\n")

    while True:
        print("Which Field you want to update:\t\n")
        p1 = input("1.Name\n2.PhoneNo.\n3.Address\n4.Class\n5.Exit\n")
        if p1 == "1":
            p2 = input("Enter the new Name:\t")
            p3 = input("Enter the Rollno of the Student:\t")
            sql = "UPDATE student SET Name = %s WHERE rollno = %s"
            v1=(p2,p3)
            mycursor.execute(sql,v1)
            mydb.commit()
            print("Data Updated\n")

        elif p1 == "2":
            p4 = input("Enter the new Phone Number:\t")
            p5 = input("Enter the Rollno of the Student:\t")
            sql = "UPDATE student SET Phone = %s WHERE rollno = %s"
            v2=(p4,p5)
            mycursor.execute(sql,v2)
            mydb.commit()
            print("Data Updated\n")

        elif p1 == "3":
            p6 = input("Enter the new Address:\t")
            p7 = input("Enter the Rollno of the Student:\t")
            sql = "UPDATE student SET Address = %s WHERE rollno = %s"
            v3=(p6,p7)
            mycursor.execute(sql, v3)
            mydb.commit()
            print("Data Updated\n")

        elif p1 == "4":
            p8 = input("Enter the new Class:\t")
            p9 = input("Enter the Rollno of the Student:\t")
            sql = "UPDATE student SET Class = %s WHERE rollno = %s"
            v4=(p8,p9)
            mycursor.execute(sql,v4)
            mydb.commit()
            print("Data Updated\n")

        else:
            break


print("Welcome to KV Kailashahar Official Database:\n")


# * Looping to provide continuous Entry

while True:
    print("What Operation would you like to Perform")
    a = input(
        "1.ADD Data:   \n2.VIEW Data:   \n3.DELETE Data:   \n4.UPDATE Data:   \n5.EXIT:   \n")
    if a == "1":
        enterValues()
    elif a == "2":
        showData()
    elif a == "3":
        clearData()
    elif a == "4":
        updateData()
    else:
        break
