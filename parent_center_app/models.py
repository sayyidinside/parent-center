from django.db import models
from .utils import custom_id


# Create your models here.
class mapel(models.Model):
    id_mapel = models.CharField(max_length=10,
                                primary_key=True,
                                unique=True,
                                default=custom_id)
    nama = models.CharField(max_length=50)

    class jenis_mapel(models.TextChoices):
        C1 = 'C1'
        C2 = 'C2'
        C3 = 'C3'

    jenis = models.CharField(max_length=2,
                             choices=jenis_mapel.choices,
                             default=jenis_mapel.C1)
