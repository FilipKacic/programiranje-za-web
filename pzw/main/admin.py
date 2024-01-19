from django.contrib import admin
from django.contrib import admin
from .models import *

# Register your models here.
model_list = [Author, Genre, Book]
admin.site.register(model_list)