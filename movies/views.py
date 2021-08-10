from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Movie, Director


def index(request):
    return render(request, 'movies/index.html')


class DirectorsView(ListView):
    """List of directors"""
    model = Director
    queryset = Director.objects.all()
    template_name = "movies/directors.html"
    context_object_name = "directors"


class DirectorDetailedView(DetailView):
    """Full director info"""
    model = Director
    template_name = 'movies/director_detail.html'
    slug_field = "id"


class MoviesView(ListView):
    """List of movies"""
    model = Movie
    queryset = Movie.objects.all()
    template_name = "movies/movies.html"
    context_object_name = "movies"


class MovieDetailedView(DetailView):
    """Full movie description"""
    model = Movie
    template_name = 'movies/movie_detail.html'
    slug_field = "id"

