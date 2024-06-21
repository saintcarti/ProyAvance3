from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request,'index.html')


def contacto(request):
    return render(request,'indexnosotros.html')

def galery(request):
    return render(request,'indexPlanes.html')