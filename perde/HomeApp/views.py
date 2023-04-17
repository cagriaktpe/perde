from .models import Movie
from .forms import RegisterForm, LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib import messages

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
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return render(request, 'register.html', {'form': form})

            newUser = User(username=username, email=email, password=password)
            newUser.save()

            auth_login(request, newUser)
            
            messages.info(request, f"You are now logged in as {username}")

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
                messages.info(request, f"You are now logged in as {username}")
                return render(request, 'login.html', {'form': form})
            auth_login(request, user)
            messages.info(request, f"You are now logged in as {username}")

            return redirect('home')

    context = {'form': form}
    return render(request, 'login.html', context)

def logout(request):
    auth_logout(request)
    messages.info(request, 'Logged out successfully!')
    return redirect('home')