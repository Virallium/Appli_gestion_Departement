from django.db import models
from django.utils import timezone
from django.conf import settings

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
    adresse=models.CharField(max_length=150,default="Mfinda, 12,Ngafula, Ngaliema")
    photo=models.ImageField(upload_to='membres/', blank=True, null=True)
    def __str__(self):
        return f"{self.nom_membre} {self.postnom_membre}"
     
    
class Activites(models.Model):
    IdAct=models.AutoField(primary_key=True)
    titre=models.CharField(max_length=100, verbose_name="Titre", default="Formation")
    nombre_participants=models.IntegerField(verbose_name="Nombre des participants", default="30")
    date=models.DateField(verbose_name="Date")
    description_de_la_formation=models.CharField(max_length=150, verbose_name="Description de la formation", default="formation sur l'évangélisation")
    img=models.ImageField(upload_to="activites/", verbose_name="Image",blank=True, null=True)
    
    def __str__(self):
        return self.titre

class versets(models.Model):
    theme=models.CharField(max_length=100, verbose_name="theme")
    personnages_bibliques=models.CharField(max_length=250, verbose_name="personnages_biblique")
    ref_biblic=models.CharField(max_length=100, verbose_name="reference biblique")
    date_publiee=models.DateField(auto_now_add=True)
    description=models.CharField(max_length=150, verbose_name="description")
    def __str__(self):
        return self.theme

class Admin(models.Model):
    IdAdmin=models.AutoField(primary_key=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='admin_custom')
    nomAd=models.CharField(max_length=100,verbose_name="nom utilisateur",default='miradi')
    id_membre=models.ForeignKey(Membres, verbose_name="Id membre", on_delete=models.CASCADE)
    IdAct=models.ForeignKey(Activites, verbose_name="Id Activite", on_delete=models.CASCADE)
    id=models.ForeignKey(versets, verbose_name="Id verset", on_delete=models.CASCADE)   
    def __str__(self):
        return self.nomAd

class Messages(models.Model):
    id_message=models.AutoField(primary_key=True)
    nom=models.CharField(max_length=100, verbose_name="Nom et Post-nom")
    message=models.TextField(verbose_name='Message', null=True, blank=True)
    telephone=models.CharField(max_length=20, verbose_name="Téléphone")
    email=models.EmailField(verbose_name="Email")
    adresse=models.CharField(max_length=150, verbose_name="Adresse physique")
    date_envoi=models.DateTimeField(auto_now_add=True, verbose_name="Date d'envoi")
    
    def __str__(self):
        return f"{self.nom} - {self.date_envoi}"
    
    class Meta:
        ordering = ['-date_envoi']
        verbose_name_plural = "Messages"

