# Item catalog Project

Game store application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own item



## Technologies used
1. sqlalchemy
2. Writing Python code with DB-API
3. Linux-based virtual machine (VM) Vagrant
4. Flask Framework





## System setup and Dependencies

To start on this project, you'll need database software (provided by a Linux virtual machine) and initial data to prepare the database.


#### Installing the dependencies and setting up the files:
1. Download [Vagrant](https://www.vagrantup.com/) and install.
2. Download [Virtual Box](https://www.virtualbox.org/) and install.
3. Download the vagrant setup files from [Udacity's Github](https://github.com/udacity/fullstack-nanodegree-vm)
These files configure the virtual machine and install all the tools needed to run this project.

5. Clone this repository to a directory of your choice.


#### Start the Virtual Machine:
1. Open Terminal and navigate to the project folders we setup above.
1. cd into the vagrant directory
1. Run ``` vagrant up ``` command to build the VM for the first time.
1. Once it is built, run ``` vagrant ssh ``` to connect.
1. cd into the correct project directory: ``` cd /vagrant/catalog ```


#### Setup the database and the pre data:
1. run ```` pytohn3 database_setup.py```` to create the database.
2. then run ````python3 intDB.py```` to fill the database with initial data.
3. now run ````python3 application.py```` to start the application.
4. Access the application locally using ```http://localhost:5000```



## Using Google Login
To get the Google login working there are a few additional steps:

1. Go to Google Dev Console and Sign up or Login.
3. Go to Credentials > Create Crendentials > OAuth Client ID
5. Select Web application
6. Enter name 'game store app'
7. Authorized JavaScript origins = ````'http://localhost:5000'````
8. Authorized redirect URIs =```` 'http://localhost:5000/login' ````&& ````'http://localhost:5000/gconnect'````
9. Select Create
10. Copy the Client ID and paste it into the data-clientid in login.html
11. On the Dev Console Select Download JSON
12. Rename JSON file to client_secrets.json
13. Place JSON file in catalog directory that you cloned from here

## Run the program
- Run this command in your terminal  ````python3 application.py````
- replace python3 with python2 if you use python ver- 2

## JSON Endpoints
The application allow the users to get the JSON :
- just access the following path: ````http://localhost:5000/game/JSON'```` and will Displays the whole catalog. Categories and all items.




