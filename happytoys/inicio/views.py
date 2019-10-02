from django.shortcuts import render, redirect
import time
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):
    print (request.user.username)
    context  = {"usuario" : "Andres Calfulef","fecha": time.strftime("%d/%m/%y")}
    return render(request,"inicio.html",context)

def descripcion(request):
    print (request.user.username)
    return render(request,"descripcion.html")

def login(request):
    if request.method == "POST":
        if ("user" in request.POST.keys()) and ("password" in request.POST.keys()):
            user = auth.authenticate(username = request.POST['user'] , password = request.POST['password'])
            print(request.POST['user'])
            print(user)
            if user is not None and user.is_active:
                auth.login(request,user)
                return redirect("/login/logueado/")
            else:
                contexto = {"error" : "error"}
                return render(request,"login.html",contexto)

        else:
            contexto = {"error" : "error"}
            return render(request,"login.html",contexto)
    return render(request,"login.html")

@login_required(login_url='/login')
def vista_logueado(request):
    if request.method == 'POST':
        if ("cerrar" in request.POST.keys()):
            auth.logout(request)
            return redirect("/login/")
    return render(request,"logueado.html")