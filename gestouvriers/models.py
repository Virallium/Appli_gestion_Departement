from django.db import models
from django.contrib.auth.models import User

class Membres(models.Model):
    IdMembre=models.AutoField(primary_key=True)
    statut_choice = (
        ("Ouvrier","Ouvrier"),
        ("Adhérent","Adhérent"),
    )
    Statut=models.CharField(max_length=20, choices=statut_choice, default="Ouvrier")
    Date_arrivee=models.DateField(verbose_name="Date arrivée")
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    
class Activites(models.Model):
    IdAct=models.AutoField(primary_key=True)
    titre=models.CharField(max_length=100, verbose_name="Titre", default="Formation")
    nombre_participants=models.IntegerField(verbose_name="Nombre des participants", default="30")
    date=models.DateField(verbose_name="Date")
    description_de_la_formation=models.CharField(max_length=150, verbose_name="Description de la formation", default="formation sur l'évangélisation")
    img=models.ImageField(upload_to="activites/", verbose_name="Image", default="activites/images_1.webp")
    
    def __str__(self):
        return self.titre
class Admin(models.Model):
    IdAdmin=models.AutoField(primary_key=True)
    emailAd=models.CharField(max_length=150, unique=True, default="admin@gmail.com")
    mpassAd=models.CharField(max_length=8, unique=True, default="Miradi000@")
    nomAd=models.CharField(max_length=100,verbose_name="nom utilisateur",default='miradi')
    postnomAd = models.CharField(max_length=100, verbose_name='Postnom', default='ndingambote')
    prenomAd = models.CharField(max_length=100, verbose_name="Prénom", default='mengi')
    IdMembre=models.ForeignKey(Membres, verbose_name="Id membre", on_delete=models.CASCADE)
    IdAct=models.ForeignKey(Activites, verbose_name="Id Activite", on_delete=models.CASCADE)
    


