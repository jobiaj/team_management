Prerequisite: 1. Python version 3.x

1. Setting up python.
sudo apt update
sudo apt -y upgrade
check the version using command. python3 -V
2. Install python-pip
sudo apt install -y python3-pip
3. Install development toold for the programming environment.
sudo apt install -y build-essential libssl-dev libffi-dev python3-dev
4. create project folder. Eg. mkdir -p /home/jobi.alungal/team_management
5. clone the project to the folder. 
cd  /home/jobi.alungal/team_management
git clone git@github.com:jobiaj/team_management.git
6. create virtual environment.
python3 -m venv team_management_project_environment
7. Activate the environment.
source team_management_project_environment/bin/activate
8. Install pip packges. Please refer requirements.txt in the team_management/conf folder.
cd team_management
pip install -r conf/requirements.txt
9. Install MySQL Database Connector
sudo apt install python3-dev
sudo apt install python3-dev libmysqlclient-dev default-libmysqlclient-dev
pip install mysqlclient
10. create database and user.
sudo mysql -u root
CREATE DATABASE team;
CREATE USER 'teamdb'@'%' IDENTIFIED WITH mysql_native_password BY 'password';
GRANT ALL ON blog_data.* TO 'teamdb'@'%';
FLUSH PRIVILEGES;
10. Add the MySQL Database Connection to our Application
Open teammanager/teammanager/settings.py

Change the settings parameters. Eg,.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'team',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'teamdb',
        'PASSWORD': 'password',
    }
}
Also change the ALLOWED_HOSTS = ['your server IP address'] in settings.py. 
You can add  ALLOWED_HOSTS = ['*'] for accepting all.
save and close the file.

11. Restart the MySQL.
sudo systemctl daemon-reload
sudo systemctl restart mysql
12. Migrate the application to create the required tables.
cd teammanager
python manage.py migrate
13. Start the application.
python3 manage.py runserver your-server-ip:8000
or
python3 manage.py runserver (Default running in 8000)
14. Check the application is up and running by accessing http://your-server-ip:8000/ in the browser.

API Details.

1. Listing team members
CURL Command: curl --location --request GET 'http://127.0.0.1:8000/team/api/v1/users/'\
SampleOutput: 

[
    {
        "id": 4,
        "firstName": "sdf",
        "lastName": "sf",
        "phone": "sdf",
        "emailId": "sf",
        "role": "REGULAR"
    },
    {
        "id": 5,
        "firstName": "sdf",
        "lastName": "sf",
        "phone": "sdf",
        "emailId": "sf",
        "role": "REGULAR"
    }
]

2. Adding team member:
CURL Command: 
curl --location --request POST 'http://127.0.0.1:8000/team/api/v1/users/' \
--header 'Content-Type: application/json' \
--data-raw ' {
        "firstName": "sSAdf1",
        "lastName": "sf",
        "phone": "sdf",
        "emailId": "sf",
        "role": 1
    }'

SampleOutput: 
{
    "id": 9,
    "firstName": "sSAdf1",
    "lastName": "sf",
    "phone": "sdf",
    "emailId": "sf",
    "role": 1
}

3. Editing a team member
CURL Command: 
curl --location --request PATCH 'http://127.0.0.1:8000/team/api/v1/user/9' \
--header 'Content-Type: application/json' \
--data-raw ' {
        "firstName": "Joby",
        "lastName": "Editted Name",
        "phone": "sdf",
        "emailId": "sf",
        "role": 1
    }'

SampleOutput: 
{
    "id": 9,
    "firstName": "Joby",
    "lastName": "Editted Name",
    "phone": "sdf",
    "emailId": "sf",
    "role": 1
}

4. Deleting a team member:
CURL Command: 
curl --location --request DELETE 'http://127.0.0.1:8000/team/api/v1/user/9' \
--header 'Content-Type: application/json' 