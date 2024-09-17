# from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django import forms
from .models import *

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')

    else:
        form = UserCreationForm()

    context = {'form': form}

    return render(request, 'registration/register.html', context)

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['user', 'book', 'rating']

class BookSearchForm(forms.Form):
    search_query = forms.CharField(max_length=255, required=False)