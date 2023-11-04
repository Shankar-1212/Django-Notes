## Django Notes App

### This is a Django-based Notes Application that utilizes the GPT API for generating text content. The application is deployed on an Amazon EC2 instance with Nginx serving the web application, accessible at http://13.233.127.144/.


## Installation 

Clone the repository:
```
git clone https://github.com/Shankar-1212/Django-Notes.git
```
Install the required dependencies:
```
pip install -r requirements.txt
```
Set up your Django environment variables, including the GPT API key.
Run the application:
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
