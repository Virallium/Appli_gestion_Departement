from django.db import models
from django.utils import timezone
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
    photo=models.ImageField(upload_to='membres/', default="activites/images_1.webp", blank=True, null=True)
    def __str__(self):
        return f"{self.nom_membre} {self.postnom_membre}"
     
    
class Activites(models.Model):
    IdAct=models.AutoField(primary_key=True)
    titre=models.CharField(max_length=100, verbose_name="Titre", default="Formation")
    nombre_participants=models.IntegerField(verbose_name="Nombre des participants", default="30")
    date=models.DateField(verbose_name="Date")
    description_de_la_formation=models.CharField(max_length=150, verbose_name="Description de la formation", default="formation sur l'évangélisation")
    img=models.ImageField(upload_to="activites/", verbose_name="Image", default="activites/images_1.webp",blank=True, null=True)
    
    def __str__(self):
        return self.titre
class Admin(models.Model):
    IdAdmin=models.AutoField(primary_key=True)
    emailAd=models.CharField(max_length=150, unique=True, default="admin@gmail.com")
    mpassAd=models.CharField(max_length=8, unique=True, default="Miradi000@")
    nomAd=models.CharField(max_length=100,verbose_name="nom utilisateur",default='miradi')
    postnomAd = models.CharField(max_length=100, verbose_name='Postnom', default='ndingambote')
    prenomAd = models.CharField(max_length=100, verbose_name="Prénom", default='mengi')
    id_membre=models.ForeignKey(Membres, verbose_name="Id membre", on_delete=models.CASCADE)
    IdAct=models.ForeignKey(Activites, verbose_name="Id Activite", on_delete=models.CASCADE)
    


