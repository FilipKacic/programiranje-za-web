from django.http import HttpResponseNotFound
from django.views import View
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.contrib.auth import logout

## Create your views here.
def not_found(request):
    return HttpResponseNotFound('<h1>Stranica nije pronađena!</h1>')

class HomePageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'main/homepage.html')

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

class RatingCreateView(CreateView):
    model = Rating
    form_class = RatingForm
    template_name = 'main/operations/add_rating.html'
    success_url = reverse_lazy('main:list')

class RatingUpdateView(UpdateView):
    model = Rating
    form_class = RatingForm
    template_name = 'main/operations/update_rating.html'
    success_url = reverse_lazy('main:list')

class RatingListView(ListView):
    model = Rating
    template_name = 'main/operations/list_ratings.html'
    context_object_name = 'ratings'

class RatingDeleteView(DeleteView):
    model = Rating
    template_name = 'main/operations/delete_rating.html'
    success_url = reverse_lazy('main:list')
    context_object_name = 'rating'
    # nepotrebno je override-ati get_context_data

def logout_view(request):
    logout(request)
    return redirect('main:homepage')
