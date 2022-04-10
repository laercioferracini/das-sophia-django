# das-sophia-django
This a POC for developing a web application using python and django framework. The intent is to experiment the aspects of using the django framework, the difficults of working with DOM elements and manipulate them.


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