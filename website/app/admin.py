from django.contrib import admin

# Register your models here.
from app.models import Lesson, User, Exercices

admin.site.register(Lesson)
admin.site.register(Exercices)
admin.site.register(User)
