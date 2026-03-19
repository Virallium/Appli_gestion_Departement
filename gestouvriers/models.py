from django.db import models
from django.contrib.auth.models import User

class formation(models.Model):
    titre=models.CharField(max_length=100, verbose_name="Titre")
    nombre_participants=models.IntegerField(verbose_name="Nombre des participants")
    date=models.DateField(verbose_name="Date")
    description_de_la_formation=models.CharField(max_length=150, verbose_name="Description de la formation")
    img=models.ImageField(upload_to="formation/", verbose_name="Image")
    
    def __str__(self):
        return self.titre


# Create your models here.
