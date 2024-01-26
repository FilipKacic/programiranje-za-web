from django.http import HttpResponseNotFound
from django.shortcuts import render
from .models import *

## Create your views here.
def not_found(request):
    return HttpResponseNotFound('<h1>Stranica nije pronađena!</h1>')

def homepage_view(request):
    return render(request, 'main/homepage.html')

def all_authors(request):
    all_authors = Author.objects.all()
    context = {'authors': all_authors}

    return render(request, 'main/authors.html', context=context)

def all_genres(request):
    all_genres = Genre.objects.all()
    context = {'genres': all_genres}

    return render(request, 'main/genres.html', context=context)

def all_books(request):
    all_books = Book.objects.all()
    context = {'books': all_books}

    return render(request, 'main/books.html', context=context)
