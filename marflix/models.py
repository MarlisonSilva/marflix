from django.db import models
from django.contrib.auth.models import User
from .validators import *
from django.conf import settings

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    age_rating = models.CharField(max_length=255)
    synopsis = models.TextField(max_length=255)
    release_year = models.PositiveIntegerField()
    language = models.CharField(max_length=255)
    duration = models.PositiveIntegerField()
    average_rating = models.FloatField()
    created_at = models.DateField(auto_now_add=True)
    poster = models.ImageField(upload_to='images/posters/', default='images/posters/default.png')
    cover = models.ImageField(upload_to='images/covers/', default='images/covers/default.png')
    media = models.FileField(upload_to='videos/', validators=[validate_video_extension])
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__ (self):
        return self.title
    
    def cover_url(self):
        return f"{settings.MEDIA_URL}{str(self.cover)}"
    
    def poster_url(self):
        return f"{settings.MEDIA_URL}{str(self.poster)}"
    
    def movie_url(self):
        return f"{settings.MEDIA_URL}{str(self.media)}"