from django.db import models
from django.utils import timezone
from movies.models import Movie, Rate


# Create your models here.


class Status(models.Model):
    """Status of the movie in the list (watching, completed, on-hold, dropped)"""
    status = models.CharField(max_length=20, default="watching")

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Statuses"


class MovieList(models.Model):
    """"User's movie list"""
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="movie")
    # profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="profile")
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name="status")
    last_change = models.DateField(default=timezone.now().date())
    rate = models.ForeignKey(Rate, on_delete=models.CASCADE, verbose_name="rate")
    access = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.movie}:{self.status}"

    class Meta:
        verbose_name = "Movie List"
        verbose_name_plural = "Movie Lists"
