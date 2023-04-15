from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Movie
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect


class LoginInterfaceView(LoginView):
    template_name = 'login.html'


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('HomeApp')
        return super().get(request,*args,**kwargs)
def home(request):
    return render(request, 'home.html', {'movies': Movie.objects.all()})

def movie(request, movie_name):
    movie_name = movie_name.lower().capitalize()
    return render(request, 'movie.html', {'movie': Movie.objects.get(title=movie_name)})