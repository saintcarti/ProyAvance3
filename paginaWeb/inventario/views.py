from django.shortcuts import render,get_object_or_404,redirect
from .models import Camara,Categoria,Marca
from .forms import CamaraForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def inventario_view(request):
    camaras = Camara.objects.all()
    context = {
        'camaras':camaras
    }

    return render(request,'vista/Mercado.html',context)

def API(request):
    return render(request,'API/indexAPI.html')
@login_required
def listado_camaras(request):
    camaras = Camara.objects.all()
    context = {
        'camaras':camaras
    }
    return render(request,'crud/listado_camaras.html',context)

def detalle_camara(request,id):
    camaraDetalle = Camara.objects.get(idCamara=id)
    
    context= {
        'camara':camaraDetalle
    }

    return render(request,'crud/detalle_camara.html',context)

def editar_camara(request,id):
    camarasModificadas = get_object_or_404(Camara,idCamara= id)
    
    if request.method == 'POST':
        categoria_id = request.POST.get('categoria')
        categoria = get_object_or_404(Categoria, idCategoria=categoria_id)

        marca_id = request.POST.get('marca')
        marca = get_object_or_404(Marca, idMarca=marca_id)

        camarasModificadas.nombreCamara = request.POST.get('nombreCamara')
        camarasModificadas.precio = request.POST.get('precio')
        camarasModificadas.descripcion = request.POST.get('descripcion')
        camarasModificadas.categoria = categoria
        camarasModificadas.marca = marca

        if 'imagen' in request.FILES:
            camarasModificadas.imagen = request.FILES['imagen']

        camarasModificadas.save()
    
    categoria = Categoria.objects.all()
    marca = Marca.objects.all()
    context= {
        'camaraModificadas':camarasModificadas,
        'categorias':categoria,
        'marcas':marca
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