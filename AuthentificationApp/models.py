from django.db import models
from django.contrib.auth.models import User

class Utilisateur(models.Model):
    nomUt=models.CharField(max_length=100,verbose_name="nom utilisateur",default='miradi')
    postnom = models.CharField(max_length=100, verbose_name='Postnom', default='ndingambote')
    prenom = models.CharField(max_length=100, verbose_name="Prénom", default='mengi')
    email = models.EmailField(verbose_name='Adresse e-mail',default='mengimiradi@gmail.com')
    motdepasse = models.CharField(max_length=100, verbose_name="Mot de passe", default='Miradi000@')


    def __str__(self):
        return f"{self.nomUt} {self.postnom} {self.prenom}"

class profil(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    adresse=models.CharField(max_length=200, verbose_name='Adresse', default='51, Kisantu-Kinshasa, Selembao')
    numero = models.CharField(max_length=20, verbose_name='Numéro de téléphone', default='0901717545')
