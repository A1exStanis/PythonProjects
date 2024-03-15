from django.shortcuts import render
from .models import Movie


def show_all_movie(request):
    movies = Movie.objects.all()
    return render(request, 'movie_app/all_movie.html', {
        'movies': movies
    })