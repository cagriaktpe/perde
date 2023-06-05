from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver


from django.db.models.signals import pre_save
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #custom_field = models.CharField(max_length=100)
    ad = models.CharField(max_length=50)
    soyad = models.CharField(max_length=50)
    dogum_tarihi = models.DateField(null=True, blank=True)
    # Diğer profil alanlarını burada tanımlayabilirsiniz (örneğin: ad, soyad, doğum tarihi, vb.)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if self.ad != self.user.first_name:
            self.user.first_name = self.ad
            self.user.save()
        if self.soyad != self.user.last_name:
            self.user.last_name = self.soyad
            self.user.save()
        super().save(*args, **kwargs)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

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
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment


