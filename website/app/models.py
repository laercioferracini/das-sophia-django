from django.db import models


class Lesson(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=10000, null=True)
    date_creation = models.DateField(auto_now=True)
    date_update = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.title}"


class Exercice(models.Model):
    statement = models.CharField(max_length=300)
    sentence = models.TextField(null=True)
    datecreation = models.DateField(auto_now=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.statement} from lesson {self.lesson.title}"


class Answer(models.Model):
    exercise = models.ForeignKey(Exercice, on_delete=models.CASCADE)


class User(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=15)
    email = models.EmailField(max_length=30, null=True)
    passwd = models.CharField(max_length=100)

