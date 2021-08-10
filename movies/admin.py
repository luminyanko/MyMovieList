from django.contrib import admin
from .models import Genre, Director, Movie, Rate, MovieRating

# Register your models here.
admin.site.register(Genre)
admin.site.register(Director)
admin.site.register(Movie)
admin.site.register(Rate)
admin.site.register(MovieRating)
