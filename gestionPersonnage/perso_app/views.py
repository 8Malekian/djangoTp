from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import Personnage
from .forms import PersonnageModelForm
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
def create(request):

    if request.method == 'GET':
        template = loader.get_template("gestionPersonnage/create.html")
        form = PersonnageModelForm()
        context = {"form":form,"typeEnvoi":"create",}
        print(request.META.get('HTTP_REFERER'))
    elif request.method == 'POST':
        template = loader.get_template("gestionPersonnage/create.html")
        context={"form":PersonnageModelForm(request.POST),
        "typeEnvoi":"create"}
        if context["form"].is_valid():
            c = context["form"].save()
    return HttpResponse(template.render(context,request))
    
def update(request,pk):
    personnage = get_object_or_404(Personnage,pk=pk)
    form = PersonnageModelForm(request.POST or None, instance=personnage)
    template = loader.get_template("gestionPersonnage/update.html")
    context = {"form":form,"typeEnvoi":"update","pk":pk}
    if form.is_valid():
        s = form.save()
    return HttpResponse(template.render(context,request))