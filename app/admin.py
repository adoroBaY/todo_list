from django.contrib import admin

from .models import *


class TodoAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'isDone')


admin.site.register(ToDo)
