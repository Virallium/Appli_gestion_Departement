from django.contrib.auth import admin
from .models import Membres, Activites, versets
from django import forms

class CustomMembers(forms.ModelForm):
    class Meta:
        model= Membres
        fields=['statut','nom_membre','prenom_membre','postnom_membre','datenais','numtel','adresse','photo']

class CustomActivities(forms.ModelForm):
    class Meta:
        model=Activites
        fields='__all__'

class CustomVersets(forms.ModelForm):
    class  Meta:
        model=versets
        fields='__all__'
        
        
        
    
    
