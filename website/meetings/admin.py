from django.contrib import admin

# Register your models here.
from meetings.models import Meeting

admin.site.register(Meeting)
