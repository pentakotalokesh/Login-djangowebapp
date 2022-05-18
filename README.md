# Django for Beginners

<ol>
  <li>Introduction</li> 
  <li>Installation</li>
  <li>Django Project</li>
  <li>Django app</li>
  <li>Deployment</li>

## Introduction

  Django is a python webframework used to create a webapps.
  It consists of predefined modules for Backend
  The Latest Version of the Django webframework is 4.0 
  Django has a Large community

## Installation

  <ul>
    <li>Python 3.7</li>
    <li>django package </li>
    <li>Virtual Environment </li>
   </ul>

   Sources:

   Python-3.7 https://www.python.org/downloads/

   After Installation of python 
   Django in Windows

   Execute commands in commandprompt(cmd.exe)

   ```
   $ pip install django
   $ pip install virtualenvwrapper -win
   ```
   we need to create virtual environment

   ```
   $ mkvirtualenv (userdefined_name)
   ```
  Again Execute command in virtual environment

  ```
   $ pip install django
   ```
  Create a directory for your Project
  change to the directory
  ```
  cd dir_name
  ```
## django project
  
  To start the django project we need to execute the following command
  
  ```
  $ django-admin startproject project_name
  ```
  it automatically creates project folder on root-director with below files
  
  ```
  _init_.py
  asgi.py
  settings.py
  urls.py
  wsgi.py
  ```
  This Files helps to Manipulate the whole databases,settings,urls of the Project
  
## django app
  
  django app is a subset of project we can have number of apps to the single project
  To create Django app we need to execute the Following command on Virtual Environment
  
  ```
  $ python manage.py startapp app_name
  ```
  
  After starting the app it creates another folder with appname that folder consists of below files
  
  ```
  migrations
  _init_.py
  admin.py
  apps.py
  models.py
  tests.py
  views.py
  ```
  Check the app is working or not
  
  ```
  python manage.py runserver
  ```
  it runs on the local server
  
# Deployed
  Check it out this Project at
  
  [link]registeryou.herokuapp.com
 

