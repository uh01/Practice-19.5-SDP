# album/models.py
from django.db import models
from musician.models import MusicianModel
from django.contrib.auth.models import User

class AlbumModel(models.Model):
    album_name = models.CharField(max_length=100)
    musician = models.ForeignKey(MusicianModel, on_delete=models.CASCADE)
    release_date = models.DateField()
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.album_name