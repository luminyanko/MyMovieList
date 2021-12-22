from django.db import models
from django.utils import timezone
from movies.models import Movie, Rate
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.


from moviemanager.settings import MEDIA_ROOT

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


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    level = models.IntegerField(default=0)
    exp = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
