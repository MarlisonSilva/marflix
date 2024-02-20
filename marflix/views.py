from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
# Create your views here.

@login_required
def home(request):
    movies = Movie.objects.all()
    return render(request, 'home/home.html', {'movies': movies})

@login_required
def movie_create(request):
    form = MovieForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.instance.user = request.user
        form.save()
        return redirect('home')
    return render(request, 'movie/movie_create.html', {'form': form})
