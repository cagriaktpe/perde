import re
from .models import Movie
from .forms import RegisterForm, LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib import messages
from .filters import FilterMovie

def searchMovie(request):
    movie = Movie.objects.all()
    filters = FilterMovie(request.GET, queryset= movie)
    context = {'filters': filters }
    return render(request,'searchMovie.html',context)


def home(request):
    return render(request, 'home.html', {'movies': Movie.objects.all()})

def movie(request, movie_name):
    movie_name = movie_name.lower().capitalize()
    return render(request, 'movie.html', {'movie': Movie.objects.get(title=movie_name)})

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')

            if password != password2:
                messages.info(request, 'The passwords do not match')  
                return render(request, 'register.html', {'form': form})

            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return render(request, 'register.html', {'form': form})

            newUser = User(username=username, email=email, password=password)
            newUser.save()

            auth_login(request, newUser)
            
            return redirect('home')

    context = {'form': form}
    return render(request, 'register.html', context)

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is None:
                messages.info(request, 'Username or password is incorrect')
                return render(request, 'login.html', {'form': form})

            auth_login(request, user)

            return redirect('home')

    context = {'form': form}
    return render(request, 'login.html', context)

def logout(request):
    auth_logout(request)
    messages.info(request, 'Logged out successfully!')
    return redirect('home')