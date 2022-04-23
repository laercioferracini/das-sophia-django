from django.contrib import admin

# Register your models here.
from app.models import Lesson, User, Exercice

admin.site.register(Lesson)
admin.site.register(Exercice)
admin.site.register(User)
