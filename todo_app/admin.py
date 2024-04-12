from django.contrib import admin
from .models import todoItem,Todolist

# Register your models here.
admin.site.register(todoItem)
admin.site.register(Todolist)