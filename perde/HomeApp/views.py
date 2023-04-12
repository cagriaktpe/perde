from django.shortcuts import render

from .models import Movie

def home(request):
    return render(request, 'home.html', {'movies': Movie.objects.all()})

def movie(request, movie_name):
    movie_name = movie_name.lower().capitalize()
    return render(request, 'movie.html', {'movie': Movie.objects.get(title=movie_name)})