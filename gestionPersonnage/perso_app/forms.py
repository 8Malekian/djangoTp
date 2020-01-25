from django import forms
from .models import Personnage


class PersonnageModelForm(forms.ModelForm):
    class Meta:
        model=Personnage
        fields = ("nom","classe","force","dexterite","constition","intelligence","sagesse","charisme","poids","user")
        

    