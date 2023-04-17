from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login, logout
from .models import Movie
from .models import *
from .forms import CreateUserForm


def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'register.html',{'form':form})

def loginPage(request):
    return render(request,'login.html',{})

def home(request):
    return render(request, 'home.html', {'movies': Movie.objects.all()})

def movie(request, movie_name):
    movie_name = movie_name.lower().capitalize()
    return render(request, 'movie.html', {'movie': Movie.objects.get(title=movie_name)})