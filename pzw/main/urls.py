from django.urls import path
from .views import *
from . import views

app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path('', views.homepage_view, name='homepage'),
    path('authors/', all_authors, name='authors'),
    path('genres/', all_genres, name='genres'), 
    path('books/', all_books, name='books'),
    path('add/', RatingCreateView.as_view(), name='add'),
    path('list/', RatingListView.as_view(), name='list'),
    path('update/<int:pk>/', RatingUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', RatingDeleteView.as_view(), name='delete'),
    path('logout/', views.logout_view, name='logout'),
]
