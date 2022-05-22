from django.db import models

# Create your models here.


TITLE_CHOICES = [
    ("Junior Software Engineer"),
    ("Middle Level Software Engineer")
]

class Movie(models.Model):
    movie_title = models.CharField(max_length=150)
    release_year = models.IntegerField()
    movie_poster = models.ImageField(upload_to = 'images/', null=True, blank=True)

    def __str__(self):
        return self.movie_title


class Blog(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_description = models.TextField(max_length=500)
    pub_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.blog_title


class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, ) # choices = TITLE_CHOICES
    birth_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.name