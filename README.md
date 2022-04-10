# das-sophia-django
This a POC for developing a web application using python and django framework. The intent is to experiment the aspects of using the django framework, the difficults of working with DOM elements and manipulate them.

# Developing

Start a project

```django-admin startproject website```

Move to website folder

```cd website```

The basic flow

**Create a web page**
 - Create a django app
 - Add a view function
 - Assing a URL
 - Run and view the page

 **Create a django app**

```python manage.py startapp app```

Delete files admin, apps, models, tests and migrations folder 

**Add a view function**
In the views.py, create a function that returns an HttpResponse 

**Assing a URL**
- In the website/urls.py, add the path to the function (Ex: path('', welcome)). *Don't forget to import the function*
- In the website/settings.py, add the 'app' in the array INSTALLED_APPS

**Run and view the page**
```python manager.py runserver```

**Setting up a Data Model**

- Create Django model classes
- Create and run migrations
- Edit data with admin interface

### Migrate changes in database



Create a model

Create a class passing models.Model as argument

Tell to django makemigrations

```python manage.py makemigrations```

To run a specific migration

```python manage.py sqlmigrate meeting 0001```

Create a superuser to connect in the admin page

```python manage.py createsuperuser```

Register a model 
in the website/meeting/admin.py add this lines

```
from meetings.models import Meeting

admin.site.register(Meeting)
```

Run the server and check the model in the admin page.


**Migration Workflow**
#### Important: Make sure your app is in INSTALLED_APPS 
Step 1: Change model code
Step 2: Generate migration script (check it)
```
python manage.py makemigrations
```
Step 3: Run migrations
```
python manage.py migrate
```

To see the migrations

``` python manage.py showmigrations```

To check the migrations, connect to the db

``` 
python manage.py dbshell

select * from django_migrations;

```

---
## Important commands for dealing with virtual environments

Check version of python

``` python --version ```

The output: 
>  Python 3.10.2

Install pip according to the python version

Creating virtual environment

```python -m venv venv```

Activate the venv
```. venv/bin/activate ```

Install a package 

```python -m pip install django```

Upgrade to latest version

```python -m pip install -U django```

Upgrade pip 

```python 
python-m pip install -U pip
```

Saving the venv (best practice)

```python -m pip freeze > requirements```

To leave the venv
```deactivate```

To install the requirements package list

```python -m pip install -r requirements.txt```