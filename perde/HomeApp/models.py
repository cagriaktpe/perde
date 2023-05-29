from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=100)
    birth_day = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name

class Actor(models.Model):
    name = models.CharField(max_length=100)
    birth_day = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    year = models.IntegerField()
    rating = models.FloatField()
    genre = models.ManyToManyField(Genre, related_name='movies')
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies')
    actors = models.ManyToManyField(Actor, related_name='movies')
    runtime = models.IntegerField()
    poster = models.CharField(max_length=200)
    trailer = models.CharField(max_length=200, null=True)
    link = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.title

class Rating(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='User')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    rating = models.IntegerField()
    def __str__(self):
        return str(self.rating)

class Watchlist(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='User')
    movies = models.ManyToManyField(Movie, related_name='watchlists')
    def __str__(self):
        return self.user.username

class Comment(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='User')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    comment = models.TextField()
    def __str__(self):
        return self.comment





