from .models import Membres, Activites, versets, Messages
from django import forms
from django.contrib.auth.models import User

class CustomMembers(forms.ModelForm):
    class Meta:
        model= Membres
        fields=['statut','nom_membre','prenom_membre','postnom_membre','photo']

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
class ContactForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['user', 'telephone', 'email', 'adresse', 'message']
        labels = {
            'user': 'user',
            'telephone': 'Téléphone',
            'email': 'Email',
            'adresse': 'Adresse physique',
            'message': 'Message'
        }