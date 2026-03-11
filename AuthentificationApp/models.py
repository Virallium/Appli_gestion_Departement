from django.db import models

class Utilisateur(models.Model):
    nomUt=models.CharField(max_length=100,verbose_name="nom utilisateur",default='miradi')
    nom = models.CharField(max_length=100, verbose_name='Nom', default='mengi')
    postnom = models.CharField(max_length=100, verbose_name='Postnom', default='ndingambote')
    prenom = models.CharField(max_length=100, verbose_name="Prénom", default='mengi')
    numero = models.CharField(max_length=20, verbose_name='Numéro de téléphone', default='0901717545')
    email = models.EmailField(verbose_name='Adresse e-mail',default='mengimiradi@gmail.com')
    motdepasse = models.CharField(max_length=100, verbose_name="Mot de passe", default='Miradi000@')

    def __str__(self):
        return f"{self.nom} {self.posnom} {self.prenom}",

