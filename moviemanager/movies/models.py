from django.db import models
from PIL import Image


# Create your models here.
class Genre(models.Model):
    """Movie genre"""
    name = models.CharField("Genre", max_length=150)
    description = models.TextField("Description")
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"


class Director(models.Model):
    """Movie directors"""
    name = models.CharField("Name", max_length=150)
    description = models.TextField("Description")
    age = models.PositiveSmallIntegerField("Age", default=0)
    image = models.ImageField("Image", upload_to="directors/", default="movies/default_poster.png")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Director"
        verbose_name_plural = "Directors"

    def save(self, *args, **kwargs):
        super(Director, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 356 or img.width > 225:
            output_size = (225, 356)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Movie(models.Model):
    title = models.CharField("Title", max_length=150)
    description = models.TextField("Description", default="")
    poster = models.ImageField("Poster", upload_to="movies/", default="movies/default_poster.png")
    year = models.PositiveSmallIntegerField("Year")
    director = models.ManyToManyField(Director, verbose_name="director", related_name="movie_director")
    genres = models.ManyToManyField(Genre, verbose_name="genres")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

    def save(self, *args, **kwargs):
        super(Movie, self).save(*args, **kwargs)

        img = Image.open(self.poster.path)

        if img.height > 356 or img.width > 225:
            output_size = (225, 356)
            img.thumbnail(output_size)
            img.save(self.poster.path)


class Rate(models.Model):
    value = models.PositiveSmallIntegerField("Value", default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Rate"
        verbose_name_plural = "Rates"


class MovieRating(models.Model):
    """Movies and their rates"""
    rate = models.ForeignKey(Rate, on_delete=models.CASCADE, verbose_name="star")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="movie")

    def __str__(self):
        return f"{self.movie}: {self.rate}"

    class Meta:
        verbose_name = "Movie Rating"
        verbose_name_plural = "Movies Rating"

