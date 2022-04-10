from django.db import models


class Lesson(models.Model):
    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=300)
    datecreation = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.title}"


class Phrases(models.Model):
    content = models.CharField(max_length=300)
    datecreation = models.DateField(auto_now=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.content} from lesson {self.lesson.title}"


class User(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=15)
    email = models.EmailField(max_length=30, null=True)
    passwd = models.CharField(max_length=100)

