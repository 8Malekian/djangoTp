from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import Personnage
# Create your views here.


def home(request):

    template = loader.get_template("gestionPersonnage/home.html")
    context = {
        "homeText": "Accueil",
    }
    return HttpResponse(template.render(context, request))
def liste(request):

    template = loader.get_template("gestionPersonnage/liste.html")
    personnages = Personnage.objects.all()
    context = {"personnages":personnages}
    return HttpResponse(template.render(context,request))

def detail(request,pk):

    template = loader.get_template("gestionPersonnage/detail.html")
    personnage = get_object_or_404(Personnage,pk=pk)
    context = {"personnage":personnage}
    return HttpResponse(template.render(context,request))