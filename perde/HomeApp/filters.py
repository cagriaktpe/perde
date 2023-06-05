import django_filters
from django.db.models import Q
from .models import Movie

class FilterMovie(django_filters.FilterSet):
    rating__gte = django_filters.NumberFilter(field_name='rating', lookup_expr='gte')
    rating__lte = django_filters.NumberFilter(field_name='rating', lookup_expr='lte')
    
    class Meta:
        model = Movie
        fields = ['director', 'genre','year','rating__gte', 'rating__lte']
        