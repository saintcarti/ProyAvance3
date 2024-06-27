from django.shortcuts import render,get_object_or_404
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
    return render(request,'crud/listado_camaras.html',context)

def detalle_camara(request,id):
    camara = get_object_or_404(Camara, id)

    context= {
        'camara':camara
    }

    return render(request,'crud/detalle_camara.html',context)

def editar_camara(request,id):
    camaras = Camara.objects.all()
    context= {

        'camaras':camaras
    }

    return render(request,'crud/editar_camara.html',context)

def crear_camara(request):
    form = CamaraForm()
    context = {
        'form':form
    }
    return render(request,'crud/crear.html',context)