from django.db import models
from django.contrib.auth.models import User

class Utilisateur(models.Model):
    Idutilisateur=models.AutoField(primary_key=True)
    email = models.EmailField(verbose_name='Adresse e-mail',default='mengimiradi@gmail.com', unique=True)
    motdepasse = models.CharField(max_length=150, verbose_name="Mot de passe", default='Miradi000@')
    def __str__(self):
        return f"{self.Idutilisateur} {self.email}"

class Profil(models.Model):
    Idprofil=models.AutoField(primary_key=True)
    nom=models.CharField(max_length=100,verbose_name="nom utilisateur",default='miradi')
    postnom = models.CharField(max_length=100, verbose_name='Postnom', default='ndingambote')
    prenom = models.CharField(max_length=100, verbose_name="Prénom", default='mengi')
    datenais=models.DateField
    numero = models.CharField(max_length=10, verbose_name='Numéro de téléphone', default='0901717545')
    photo=models.ImageField(upload_to='Profil/', default="Profil/default.png")
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    adresse=models.CharField(max_length=200, verbose_name='Adresse', default='51, Kisantu-Kinshasa, Selembao')
    
    def __str__(self):
        return f"{self.nom} {self.prenom} {self.adresse} {self.photo}"



    