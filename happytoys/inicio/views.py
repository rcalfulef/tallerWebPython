from django.shortcuts import render
import time

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
            user = auth.authenticate(user = request.POST['user'] , password = request.POST['password'])
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

@login_required(login_url = '/login')
def vista_logueado(request):
    return render(request,"logueado.html")