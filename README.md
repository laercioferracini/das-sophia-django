# das-sophia-django
This a POC for developing a web application using python and django framework. The intent is to experiment the aspects of using the django framework, the difficults of working with DOM elements and manipulate them.

# Developing

Start a project

```django-admin startproject website```

Move to website folder

```cd website```

The basic flow

**Cr
eate a web page**
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


---
## **Setting up a Data Model**

- Create Django model classes
- Create and run migrations
- Edit data with admin interface



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
## Combining Model, View, And Template

To create a template you need to create the directory templates/<appname> inside the django app folder(Ex: website/app/templates/app) 
Inside this directory you put your html files
In views.py, you return a render with the request and path of the html file
Ex: ```return render(request, "app/welcome.html")```

### Template Variable and Dynamic Content


### Urls and Link Building

URLS
- Link Building
- Named URL mappings
- URLs and apps
- For loops in templates

Ex: `{% url 'detail' meeting.id %}`
You need to add in website/urls.py file

```
path('meetings/', include("meetings.urls")),
```
And the lines below in the meetings/urls.py file in the app meetings

```
urlpatterns = [
    path('<int:id>', views.detail, name="detail"),
    path('rooms', views.rooms_list, name="rooms")
]

```

*For loops*
```
<ol>
    {% for ex in exercises %}
    <li>{{ex.content}}</li>
    {% endfor%}
</ol>
```

## Templates, Styling and static content

To put static files like css, images, etc. You need to create the structure _<appfolder>/static/<appname>/style.css_

Ex: `app/static/app/styles.css`

Add this line in the html file
```    
<link rel="stylesheet" href="{% static 'app/tailwind.css' %}">
 ```

Stop the server and start again 
Obs: In development mode you need to add ```--insecure``` in the commandline to get the static files

#### Template inheritance

Inside the templates' folder, create a html file base.html like this

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{% block title %}{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'app/style.css' %}">
</head>
<body class="your-css-classes" style="your-font-family">
{% block content%}
{% endblock %}
</body>
</html>
```

In the parents html files, you can use this lines

```html
{% extends "base.html" %}

{% block title %}Your title {{meeting.title}}{% endblock %}

{% block content %}

<p> The content is here </p>

{% endblock %}
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