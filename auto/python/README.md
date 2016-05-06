# Gurukula-python-testsuite
Python testsuite for simple Gurukula project

# Features of the application:
The application is used to maintain Branches and Staff information (can be seen from Entities Menu).

You can view, edit, delete and query both Staff and Branches.

Further, Pagination is enabled when viewing the Staff/Branch.

The logged in account information can be viewed/edited from the Account Menu.

Login/Logout as existing user

Register a new User

# Requirements:

If you don't have python 2.7 use this commands to install:
-----------------------------------------------------------
```
sudo add-apt-repository ppa:fkrull/deadsnakes
sudo apt-get update
sudo apt-get install python2.7
```

Install Python Packages:
------------------------
Note That: you may use virtual env for this step
```
python$> pip install -r req.txt
```

Run the tests
---------------
change the url parameter in config.ini
```
python$> nosetests -xv testsuite --tc-file config.ini  2>testresults.log
```

or overwrite it using the following command
```
python$> nosetests -xv testsuite --tc-file config.ini --tc=main.url:http://127.0.0.1:8080/gurukula  2>testresults.log
```
