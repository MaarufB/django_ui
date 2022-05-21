from django.db import models

# Create your models here.

class Movie(models.Model):
    movie_title = models.CharField(max_length=150)
    release_year = models.IntegerField()
    movie_poster = models.ImageField(upload_to = 'images/', null=True, blank=True)

    def __str__(self):
        return self.movie_title




