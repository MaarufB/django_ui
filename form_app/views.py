from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Movie
from .forms import MovieForm
from django.contrib import messages
# Create your views here.


def index(request):
    if request.method == 'POST':
        movie_form = MovieForm(request.POST, request.FILES)
        if movie_form.is_valid():
            movie_form.save()
            messages.success(request, "You Movie was successfully ADDED!")
        else:
            messages.error(request, "Error saving form")

        return redirect("form_app:index")

    movie_form = MovieForm()
    movies = Movie.objects.all()

    return render(
                    request=request, 
                    template_name='form_app/index.html', 
                    context={
                        'movie_form': movie_form, 
                        'movies': movies
                        })



