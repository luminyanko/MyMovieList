from django.urls import path
from . import views

urlpatterns = [
    path('', views.MoviesView.as_view(), name="movies"),
    path('directors/', views.DirectorsView.as_view(), name="directors"),
    path('movie/<int:pk>/', views.MovieDetailedView.as_view(), name="movie-detail"),
    path('director/<int:pk>/', views.DirectorDetailedView.as_view(), name="director-detail"),
]