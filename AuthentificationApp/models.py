from django.db import models
from django.contrib.auth.models import User

class Profil(models.Model):
    # On lie le profil DIRECTEMENT au système de compte Django
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profil')
    
    postnom = models.CharField(max_length=100, verbose_name='Postnom', blank=True)
    datenais = models.DateField(null=True, blank=True)
    numero = models.CharField(max_length=15, verbose_name='Numéro de téléphone', blank=True)
    
    # Pour Supabase, attention : l'image risque d'être perdue à chaque push sur Render 
    # si tu n'utilises pas Supabase Storage
    photo = models.ImageField(upload_to='Profil/', blank=True, null=True)
    
    adresse = models.CharField(max_length=200, verbose_name='Adresse', blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.user.email} - {self.user.password}"

    