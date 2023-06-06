"""perde URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import HomeApp.views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeApp.views.home, name='home'),
    path('movie/<str:movie_name>', HomeApp.views.movie, name='movie'),
    path('register/', HomeApp.views.register, name='register'),
    path('login/', HomeApp.views.login, name='login'),
    path('logout/', HomeApp.views.logout, name='logout'),
    path('searchMovie/',HomeApp.views.searchMovie, name= 'searchMovie'),
    path('searchMovie/movies/', HomeApp.views.movie, name='movie'),
    path('add-comment/<str:movie_name>', HomeApp.views.add_comment, name='add-comment'),
    path('delete-comment/<str:movie_name>/', HomeApp.views.delete_comment, name='delete-comment'),
    path('aboutus/', HomeApp.views.aboutus, name='aboutus'),
    path('rate/<str:movie_name>', HomeApp.views.rate, name='rate'),
    path('delete-rating/<str:movie_name>/', HomeApp.views.delete_rating, name='delete-rating'),
    path('profile/', HomeApp.views.profile, name='profile'),

]