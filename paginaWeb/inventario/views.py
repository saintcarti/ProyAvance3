from django.shortcuts import render
from .models import Camara
from .forms import CamaraForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def inventario_view(request):
    return render(request,'Inventario/Mercado.html')

def API(request):
    return render(request,'API/indexAPI.html')

def listado_camaras(request):
    camaras = Camara.objects.all()
    context = {
        'camaras':camaras
    }
    return render(request,'Inventario/listado_camaras.html',context)