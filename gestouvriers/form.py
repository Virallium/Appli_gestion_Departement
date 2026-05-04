from .models import Membres, Activites, versets
from django import forms
from django.contrib.auth.models import User

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
        
class CustomActivites(forms.ModelForm):
    class Meta:
        model=Activites
        fields='__all__'
class Custome_Versets(forms.ModelForm):
    class Meta:
        model=versets
        fields='__all__'
        
        
class loginAdmin(forms.Form):
    username = forms.CharField(max_length=150, label='Nom d’utilisateur')
    password = forms.CharField(widget=forms.PasswordInput, label='Mot de passe')

class ChangePassword(forms.ModelForm):
    class Meta:
        model=User
        fields=['password']