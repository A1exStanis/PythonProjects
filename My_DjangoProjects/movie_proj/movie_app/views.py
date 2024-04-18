from django.shortcuts import render, get_object_or_404
from .models import Movie, Actor, Director
from django.db.models import F, Max, Min, Avg, Count, Sum, Value


def show_all_movie(request):
    # movies = Movie.objects.order_by(F('year').asc(nulls_first=True),'rating')
    movies = Movie.objects.annotate(year_rating=F('year') + F('rating'))
    agg = movies.aggregate(Count('id'), Avg('budget'), Max('rating'), Min('rating'))
    return render(request, 'movie_app/all_movie.html', {
        'movies': movies,
        'agg': agg
    })


def show_one_movie(request, slug_movie):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', {
        'movie': movie
    })


def show_all_directors(request):
    directors = Director.objects.all()
    return render(request, 'movie_app/all_director.html',
                  {'directors': directors})


def show_one_director(request, id_director: int):
    director = get_object_or_404(Director, id=id_director)
    return render(request, 'movie_app/one_director.html', {
        'director': director
    })


def show_all_actors(request):
    actors = Actor.objects.all()
    return render(request, 'movie_app/all_actors.html',
                  {'actors': actors})


def show_one_actor(request, id_actor: int):
    actor = get_object_or_404(Actor, id=id_actor)
    return render(request, 'movie_app/one_actor.html', {
        'actor': actor
    })