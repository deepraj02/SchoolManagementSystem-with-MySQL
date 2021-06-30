
# School Management System with MySQL Integration 🔥

## This is a School Management System made using Python and MySQL.
This Repository Contains both the GUI version and the CLI version of the Project

## Documentation
There are a total of 5 GUI python files and 1 CLI file in this project. 
The Project files Include the Following with their uses along with them.

    1.	main.py Project file containing the CLI(Command Line Interface) Version of “School Management System” Project.

    2.	Resource Folder(res) which Contains the resources(icons) for the GUI(Graphical User Interface) Version of the Project.

    3.	GUI Files:-
	        mainGuiFile.py- This File Contains the Main menu Layout of the overall GUI Project.
        	dataEntryFile.py- This File connects the User Interface with the MySQL Database and takes input of Data from the user and stores in the Database.
        	deleteDataFile.py- As the name suggest this File is for deleting the Data from the DataBase.

        	updateDataFile.py- This file is for Updating the existing data. It takes input from the user and Updates the data using the RollNo. Which is also the Primary Key of the Database.

	        viewDataFile.py- This UI file helps us to view the Overall existing data by running SQL Queries from the Python Script.

## PROJECT PREREQUISITES: -
The Modules you need to run this program on your system are as follows:

    1. Tkinter
    2. mysqlconnector

## DATABASE CONNECTION

Copy and Paste this code in your MySQL Editor before running the Program.


    Also, we need to create a Database which in our case is MySQL.
    After creating the Database, we have to create 1 table to store the data of books present in the School.

    Use the Following Commands to create the Database and Tables which are required by our Project.
	
        •    create database SchoolManagement;
        •	create table student (RollNo varchar (20) primary key, Name varchar (30), Class varchar (30), Phone varchar (30), Address Varchar(1oo))

    



  
## Authors

- [@DeeprajBaidya](https://www.github.com/deepraj02)

  
## Badges


[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)

## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.

  
## Installation 

Download this Repository in your System and then follow the Documentation and you are good to go.

```bash 
    git clone https://github.com/deepraj02/SchoolManagementSystem-with-MySQL.git
    cd SchoolManagementSystem-with-MySQL
    python main.py
```
    
    
