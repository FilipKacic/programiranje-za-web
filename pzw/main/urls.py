from django.urls import path
from .views import *

app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path('', homepage_view, name='homepage'),
    path('authors', all_authors, name='authors'),
    path('genres', all_genres, name='genres'),
    path('books', all_books, name='books'),
]