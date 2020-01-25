from django.contrib import admin
from .models import Personnage

# Register your models here.
class PersonnageGestion(admin.ModelAdmin):
    list_display = ("pk","nom","classe","force","dexterite","constition","intelligence",
    "sagesse","charisme","poids","user")

admin.site.register(Personnage,PersonnageGestion)