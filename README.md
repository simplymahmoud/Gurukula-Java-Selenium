# Gurukula-Testsuite
Gurukula testsuite for simple website


# Instructions:
The application (gurukula) is written in Java and is available at: https://github.com/PA-Reporting/staff
You can launch the application using: java –jar .war
Note: Please use Java 1.8 to access the application. Username: admin Password: admin


# Features of the application:

The application is used to maintain Branches and Staff information (can be seen from Entities Menu). 

You can view, edit, delete and query both Staff and Branches. 

Further, Pagination is enabled when viewing the Staff/Branch. 

The logged in account information can be viewed/edited from the Account Menu. 

Login/Logout as existing user

Register a new User

# What needs to be done:
Please use any language or framework (preferably Selenium) of your preference to automate the various use cases. Upload your automation tests to a Git hub location and share this information when done. Please add information with respect to framework, tests covered, how to launch automation tests  and any other information to a document in the same Git hub location. 


# Folders:

manual: for manual test cases.

auto: for auto test cases written in (python, java, js).

auto/testplan: containing the test plan suggested for the testsuites to cover the usecases.

# Idea: 
It was prefered to do it in Java/Selenium with junit or testng but after I made a good research I found that it will not be the best solution. As the project using AngularJs so the best solution is to use Protractor with any java script test framework like jasmine/cucumberjs/moca/karma, I made it with Jasmine. I found that we have another solution to test this project based on python/selenium/unittest but not pure selenium it's through pytractor, so I use it too.

Testplan and test cases- > finished

# Used technologies:
Java/Selenium-junit -> in progress

Python/Selenium/Pytractor-unittest - > finished

JavaScript/Protractor-Jasmine -> stopped

# Known issues:
1- Register new user.

2- Edit logged user settings and password.

3- Delete (branch) assigned with existing (staff) needs proper error message.

4- No Paging in (branch).

5- Login automatically feature not working. 