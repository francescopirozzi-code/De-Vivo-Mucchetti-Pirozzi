Pre-Use Warnings: Context and License
-------------------------------------
This README file serves as a guide for the correct execution and display of the website, which functions as an exam project for the "Web Technologies" course at the University of Naples "Parthenope" for the academic year 2024/2025. Before describing the steps to follow, we advise that this project is distributed under the Apache 2.0 license (see the LICENSE file for further details).

Pre-Use Warnings: Copyright Declaration
---------------------------------------
This project is protected under the following copyright notice:

Copyright 2025 RottaNautica

Pre-Use Warnings: Terms of Use
------------------------------
The use, reproduction, and distribution of this project are permitted only in accordance with the terms of the Apache 2.0 license. It is not permitted to use or distribute this project as your own without proper attribution and compliance with the terms of the license.

For further information, please consult the LICENSE file included in this repository.

Pre-Use Warnings: Additional Information
----------------------------------------
Given all that is stated in the preceding lines, if you accept the Terms of Use and act in accordance with the Copyright that protects this project, for the correct execution and display, continue reading this file and be sure to execute the steps described below in order and to the letter.

Project Name: RottaNautica

Project Description
-------------------
The project aims to offer a comprehensive platform for the online sale of nautical products, including catalog management and user management. The goal of "RottaNautica", which is the name of the site, is to create an intuitive and secure online shopping experience for enthusiasts of nautical activities.

Installation and Execution
--------------------------
Below there is a detailed description of the programs to download and the steps to follow to correctly run the website.


STEP 1 (mandatory)
------------------
Installation of the programs necessary for execution
----------------------------------------------------
To correctly run the project, it is necessary to install the following programs:

Mandatory
---------
Python (from the Python.org website);

P.S. Be sure to check the "Add Python to PATH" option. This option adds Python to the system PATH, which means that it will be possible to execute Python commands from any directory in the terminal or command prompt without having to specify the full path of the Python executable.

SQL Lite (from the website https://sqlitebrowser.org/dl/);

P.S. For the realization of the project, the version "DB Browser for SQLite - Standard installer for 64-bit Windows" was used.

Visual Studio Code (from the website https://code.visualstudio.com/ or from the Microsoft Store).

Optional
--------
DIA (from the website http://dia-installer.de/)


STEP 2 (mandatory)
------------------
Downloading the necessary files
-------------------------------
Download ALL the files present in the repository, making sure NOT to forget any of them and NOT to move any files inside or outside their respective folders. Furthermore, it is absolutely necessary NOT to rename the folders and/or files with other names, as the paths have already been defined with the current names.

Technologies used: Please note that the technologies used for the realization of this project are HTML5, CSS3, Python, Flask, SQL Alchemy, and SQL Lite.


STEP 3 (optional)
-----------------
Visualization of the database architecture
------------------------------------------
N.B. This step is optional, as it is NOT NECESSARY for the correct execution of the website. If you decide to execute it, we inform you that it is necessary to have installed "DIA" in step 1. Otherwise, it will not be possible to view the file.

It is possible to view the architecture of the database that manages the website. The architecture of the database is shown by the file RottaNautica_database (which has the extension .dia).


STEP 4 (mandatory)
------------------
Execution of the website
------------------------
For the correct execution and display of the website, follow the steps below in order:

1) Launch "Visual Studio Code";

2) Click on the "Extensions" section on the left (square icon, third icon from the bottom), search for and install the "Python" extension from "Microsoft";

3) Download "SQLAlchemy" and "Flask" from the terminal, executing the following commands separately:

pip install sqlalchemy

pip install flask

To do this, it is necessary to open the terminal of the operating system you are using and select the folder where all the downloaded files are located. For example, for Windows, it will be something like this:

C:\Users\Username\OneDrive\Desktop\Computer Resources\Personal\University\THIRD_YEAR\Web_Technologies\RottaNautica>

After writing this, execute the commands indicated above separately and in order;

4) Return to "Visual Studio Code" and click on the "File" section at the top left, select the "Open Folder" option and choose the folder where the files "database.py" and "app.py" are located;

5) Once the folder is selected, execute the file "database.py" first and then the file "app.py" in order;

6) Once the file "app.py" is executed, a link to the website will be returned in the output;

7) Click on the link and test the project, for example, by creating an account and trying to log in.

TEST WITH SQL LITE
------------------
To verify the correct functionality of the database, it is possible to open both the website and the SQL Lite window at the same time and try to register a user account. Follow these steps in order:

1) Run the SQL Lite setup and install the program;

2) Launch the program and click on the "Open Database" option and select the file named "database", which has the extension .db, from the folder containing the files installed from the repository;

3) Once the database is open, click on the "Browse Data" section, click on the down arrow that opens the drop-down menu next to the text "Table:" and select the table named "Users".


