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

 Create a django app

```python manage.py startapp app```

Delete files admin, apps, models, tests and migrations folder 

In the views.py, create a function that returns an HttpResponse 

In the website/settings.py, add the 'app' in the array INSTALLED_APPS

In the website/urls.py, add the path to the function (Ex: path('', welcome)). *Don't forget to import the function*

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