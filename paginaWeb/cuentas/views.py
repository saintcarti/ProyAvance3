from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import UserProfile



def iniciosesion(request):

    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        clave = request.POST.get('pass')
        
        user = authenticate(request, username= usuario , password= clave)

        if user is not None:
            profile = UserProfile.objects.get(user=user)

            request.session['perfil']= profile.role

            login(request, user)

            return redirect('inicio')
        else:
            context= {
                'error':'Error intente denuevo'
            }

            return render(request, 'registration/login.html', context)
        
    return render(request, 'registration/login.html')

def registro(request):
    return render(request, 'registration/register.html')

def exit(request):
    logout(request)
    return redirect('inicio')

def recuperar(request):
    return render(request, 'registration/recuperar.html')
