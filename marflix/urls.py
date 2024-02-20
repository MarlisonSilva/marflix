from django.urls import path
from marflix import views


urlpatterns = [
    path('', views.home, name='home'),
    path('movie/c/', views.movie_create, name='movie.create'),
]

