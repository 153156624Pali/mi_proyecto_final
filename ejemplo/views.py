from colorama import reinit
from django.shortcuts import render
from ejemplo.models import Familiar
def index(request):
    return render(request, "ejemplo/saludar.html",{"nombre":"Fabrizzio", "apellido":"crescini"})
    
def index_dos(request):
    return render(request, "ejemplo/saludar.html",
    {"notas":[1,2,3,4,5,6,7,8,9]}
    )


def imc(request, peso, altura):
    imc = peso / (altura**2)
    return render(request, "ejemplo/imc.html",{"imc":imc, 
    "peso":peso,
    "altura":altura})

def monstrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "ejemplo/familiares.html", 
                         {"lista_familiares": lista_familiares})
                         