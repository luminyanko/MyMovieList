from django.shortcuts import render
from django.views.generic import View


from .models import Movie


def index(request):
    return render(request, 'movies/index.html')


class MoviesView(View):
    """List of movies"""
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, "movies/movies.html", {"movies": movies})
