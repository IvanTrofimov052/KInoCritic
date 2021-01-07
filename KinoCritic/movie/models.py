# ToDo: table Comments-Movie
# ToDo: table Movie-Actor

from django.db import models


# Create your models here.
class Movie(models.Model):
	movie_name = models.CharField(max_length=200)
	image_url = models.CharField(max_length=200)
	trailer_link = models.CharField(max_length=200)
	description = models.TextField()
	raiting = models.IntegerField(default=0)