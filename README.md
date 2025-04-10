Local Weather Dashboard (Django + MySQL)

A beginner-friendly weather web application built with Django that fetches live weather data using the OpenWeatherMap API and stores relevant info in a MySQL database.


1. 🔧 Features

* 🔍 Search and display current weather by city
* 📡 Uses OpenWeatherMap API for real-time data
* 💾 Stores data using MySQL (no SQLite)
* 🖼️ Clean interface using HTML + CSS (no Bootstrap)


2. Tool and technologies

* Django – Python framework to build the website
* MySQL – Stores your weather data
* HTML,CSS – For the webpage design
* OpenWeatherMap API – Provides real-time weather


3. Screenshot
Local Weather Dashboard (Django + MySQL)

4. How to install and run

a. Clone the GitHub repository 

git clone https://github.com/seethakalaivani/weather-dashboard.git

cd weather-dashboard

b. Set up a virtual environment

python -m venv venv

For Windows:

venv\Scripts\activate

c. Install required Python packages

pip install -r requirements.txt

d. Configure your MySQL database
   - Open the file: weather_dashboard/settings.py
   - Edit the DATABASES section with your MySQL credentials and DB name

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'weather_db',             # Your database name
        'USER': 'root',                   # Your MySQL username
        'PASSWORD': 'root',                 # Your MySQL password
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

e. Create the database in MySQL manually
 Login to MySQL and run:
 CREATE DATABASE weather_db;

f. Run Django migrations to create the tables
python manage.py makemigrations
python manage.py migrate

g. Add your OpenWeatherMap API key
    
api_key = "9d98929d09759871e6dc0a4d5abe2bd5"

h. Run the development server
python manage.py runserver