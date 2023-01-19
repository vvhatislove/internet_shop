# Internet Shop
***

## Project setup

### Environment variables

First you need to create a file ".env"
In this file, you need to create 7 variables, namely:
+ **DJANGO_SECRET_KEY**

Contains django secret key
+ **DB_NAME**

Contains the name of the database
+ **DB_USER**

Contains the username for the database
+ **DB_PASSWORD**

Contains the database password
+ **DB_HOST**

### Setting up a virtual environment
At the root of the project, create a virtual environment using the command:

`python3 -m venv venv`

Activate it:

`venv/bin/activate`

Then we install all the dependencies from the requirements.txt file into the virtual environment:

`pip3 install -r requirements.txt`

### Migrations
If all the previous steps are completed successfully, all that remains for you is to apply the migrations, for this we use this command:

`python3 manage.py migrate`

### Launch of the project
After successful configuration, all that remains is to write the following command to start the server:

`python3 manage.py runserver`

