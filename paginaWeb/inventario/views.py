from django.shortcuts import render,get_object_or_404,redirect
from .models import Camara
from .forms import CamaraForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def inventario_view(request):
    return render(request,'vista/Mercado.html')

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
    if request.method == 'POST':
        camaraform = CamaraForm(request.POST,request.FILES)
        if camaraform.is_valid():
            camaraform.save()
            return redirect('listado_camaras')
    else:
        camaraform = CamaraForm()

    return render(request,'crud/crear.html',{'camaraform':camaraform})

def eliminar_camara(request,id):
    camaraEliminada = Camara.objects.get(idCamara=id)
    camaraEliminada.delete()
    return redirect('listado_camaras')