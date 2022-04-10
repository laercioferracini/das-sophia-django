from django.contrib import admin

# Register your models here.
from app.models import Lesson, User, Phrases

admin.site.register(Lesson)
admin.site.register(Phrases)
admin.site.register(User)
