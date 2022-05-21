from django import forms
from .models import Movie

# Create your owm forms her

class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ('movie_title', 'release_year', 'movie_poster') #'__all__'
