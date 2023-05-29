import django_filters
from .models import Movie

class FilterMovie(django_filters.FilterSet):
    class Meta:
        model = Movie
        fields = ['director', 'genre','year','rating']
         