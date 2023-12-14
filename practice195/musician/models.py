# musician/models.py
from django.db import models

class MusicianModel(models.Model):
    id_no = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    instrument_type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"