import re
from .models import Movie
from .forms import RegisterForm, LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib import messages
from .filters import FilterMovie
from .models import Movie
from .forms import RegisterForm, LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib import messages
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password


'''@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'profile.html', {'form': form})
'''
def profile(request):
    user_profile = request.user.userprofile
    form = UserProfileForm(instance=user_profile)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Profil sayfasına yönlendirme yapabilirsiniz

    return render(request, 'profile.html', {'form': form})




def searchMovie(request):
    movie = Movie.objects.all()
    filters = FilterMovie(request.GET, queryset= movie)
    context = {'filters': filters }
    return render(request,'searchMovie.html',context)


def home(request):
    return render(request, 'home.html', {'movies': Movie.objects.all()})

def movie(request, movie_name):
    movie_name = movie_name.lower().capitalize()
    comments = Movie.objects.get(title=movie_name).comments.all()

    return render(request, 'movie.html', {'movie': Movie.objects.get(title=movie_name), 'comments': comments})

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

            #passwordu hashle
            password = make_password(password)

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

def add_comment(request, movie_name):
    movie_name = movie_name.lower().capitalize()
    movie = Movie.objects.get(title=movie_name)
    comment = request.POST.get('comment')

    if movie.comments.filter(user=request.user).exists():
        movie.comments.filter(user=request.user).update(comment=comment)
    else:
        movie.comments.create(user=request.user, comment=comment)
    return redirect('movie', movie_name=movie_name)

def delete_comment(request, movie_name):
    movie_name = movie_name.lower().capitalize()
    movie = Movie.objects.get(title=movie_name)
    movie.comments.filter(user=request.user).delete()
    return redirect('movie', movie_name=movie_name)

def aboutus(request):
    return render(request, 'about.html')

def rate(request, movie_name):
    movie_name = movie_name.lower().capitalize()
    movie = Movie.objects.get(title=movie_name)
    rate = request.POST.get('rating')

    if movie.ratings.filter(user=request.user).exists():
        movie.ratings.filter(user=request.user).update(rating=rate)
    else:
        movie.ratings.create(user=request.user, rating=rate)
    return redirect('movie', movie_name=movie_name)

def delete_rating(request, movie_name):
    movie_name = movie_name.lower().capitalize()
    movie = Movie.objects.get(title=movie_name)
    movie.ratings.filter(user=request.user).delete()
    return redirect('movie', movie_name=movie_name)
