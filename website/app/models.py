from django.db import models


class Lesson(models.Model):
    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=300)
    exercises = models.TextField
    datecreation = models.DateField


class User(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=15)
    passwd = models.TextField()

