from django.contrib import admin
from .models import *

# Register your models here.
model_list = [Author, Genre, Book, Rating]
admin.site.register(model_list)