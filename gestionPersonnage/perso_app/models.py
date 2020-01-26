from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()
# Create your models here.

class Personnage(models.Model):
    nom = models.CharField(max_length=100)
    classe = models.CharField(max_length=200)
    force = models.PositiveIntegerField(default=1,validators=[MaxValueValidator(21)])
    dexterite = models.PositiveIntegerField(default=1,validators=[MaxValueValidator(21)])
    constition = models.PositiveIntegerField(default=1,validators=[MaxValueValidator(21)])
    intelligence = models.PositiveIntegerField(default=1,validators=[MaxValueValidator(21)])
    sagesse= models.PositiveIntegerField(default=1,validators=[MaxValueValidator(21)])
    charisme= models.PositiveIntegerField(default=1,validators=[MaxValueValidator(21)])
    poids = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class Equipement(models.Model):
    nom = models.CharField(max_length=100)
    degat = models.PositiveIntegerField(default=1,validators=[MaxValueValidator(10)])
    poids = models.PositiveIntegerField(default=1)
    prix = models.PositiveIntegerField(default=1)
    Propriétés = models.TextField(max_length=1000)
