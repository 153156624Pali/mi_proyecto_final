from colorama import reinit
from django.shortcuts import render
from ejemplo.models import Familiar
from ejemplo.forms import Buscar 
from django.views import View 
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
                         


class BuscarFamiliar(View):

    form_class = Buscar
    template_name = 'ejemplo/buscar.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})

       