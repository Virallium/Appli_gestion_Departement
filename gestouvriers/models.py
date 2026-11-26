from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User

#un membre est un utilisateur donc il a un profil
class Membres(models.Model):
    id_membre=models.AutoField(primary_key=True)
    statut_choice = (
        ("Ouvrier","Ouvrier"),
        ("Adhérent","Adhérent"),
    )
    statut=models.CharField(max_length=20, choices=statut_choice, default="Ouvrier")
    date_arrivee=models.DateField(verbose_name="Date arrivée",default=timezone.now)
    nom_membre=models.CharField(max_length=100, verbose_name="Nom_Membre", default="Winner")
    prenom_membre=models.CharField(max_length=100, verbose_name="Prenom_Membre", default="Alex")
    postnom_membre=models.CharField(max_length=100, verbose_name="Postnom_Membre", default="Miyakudi")
    datenais=models.DateField(verbose_name="Date_naissance", default=timezone.now,null=True, blank=True)
    numtel=models.CharField(max_length=20, default="0901717545")
    adresse=models.CharField(max_length=150,default="Mfinda, 12,Ngafula, Ngaliema", null=True, blank=True)
    photo=models.ImageField(upload_to='membres/', blank=True, null=True, default="")
    def __str__(self):
        return f"{self.nom_membre} {self.postnom_membre}"
     
    
class Activites(models.Model):
    IdAct=models.AutoField(primary_key=True)
    titre=models.CharField(max_length=100, verbose_name="Titre", default="Formation")
    nombre_participants=models.IntegerField(verbose_name="Nombre des participants", default=30)
    date=models.DateField(verbose_name="Date", default=timezone.now)
    description_de_la_formation=models.CharField(max_length=150, verbose_name="Description de la formation", default="formation sur l'évangélisation")
    img=models.ImageField(upload_to="activites/", verbose_name="Image", blank=True, null=True, default="")
    
    def __str__(self):
        return self.titre

class versets(models.Model):
    theme=models.CharField(max_length=100, verbose_name="theme", default="Thème à définir")
    personnages_bibliques=models.CharField(max_length=250, verbose_name="personnages_biblique", default="À définir")
    ref_biblic=models.CharField(max_length=100, verbose_name="reference biblique", default="Référence à définir")
    date_publiee=models.DateField(auto_now_add=True)
    description=models.CharField(max_length=150, verbose_name="description", default="Description à définir")
    def __str__(self):
        return self.theme



class Messages(models.Model):
    id_message=models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message=models.TextField(verbose_name='Message', null=True, blank=True, default="")
    telephone=models.CharField(max_length=20, verbose_name="Téléphone", default="")
    email=models.EmailField(verbose_name="Email", default="")
    adresse=models.CharField(max_length=150, verbose_name="Adresse physique", default="")
    date_envoi=models.DateTimeField(auto_now_add=True, verbose_name="Date d'envoi")
    
    def __str__(self):
        return f"{self.user}- {self.date_envoi}"
    
    class Meta:
        ordering = ['-date_envoi']
        verbose_name_plural = "Messages"

