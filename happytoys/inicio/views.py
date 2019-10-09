from django.shortcuts import render, redirect
import time
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from cart.forms import CartAddJugueteForm
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

def inicio(request):
    print (request.user.username)
    context  = {"usuario" : "Andres Calfulef","fecha": time.strftime("%d/%m/%y")}
    return render(request,"inicio.html",context)

def descripcion(request):
    print (request.user.username)
    return render(request,"descripcion.html")

def buscador(request):
    context = {}
    if request.method == "POST":    
        if "search" in request.POST.keys():
            resultado = Juguete.objects.filter(nombre__contains = request.POST['search'])
            context = {'resultado':resultado}
    return render(request,"buscador.html",context)

def juguetes(request):
    context = {}
    if request.method == "POST":
        if "buscador" in request.POST.keys():
            resultado = Juguete.objects.filter(nombre__contains = request.POST['buscador'])
            context = {'resultado': resultado}
    
    else: # si ingremos a la URL y no realizamos ninguna busqueda
        resultado = Juguete.objects.all()
        context = {'resultado': resultado}

    return render(request,"juguetes.html",context)

def juguete_detail(request,juguete_id):
    juguete = get_object_or_404(Juguete, id=juguete_id)
    cart_juguete_form = CartAddJugueteForm()
    context = {
        'juguete': juguete,
        'cart_juguete_form': cart_juguete_form
    }
    return render(request, 'detail.html', context)



def login(request):
    if request.method == "POST":
        if ("user" in request.POST.keys()) and ("password" in request.POST.keys()):
            user = auth.authenticate(username = request.POST['user'] , password = request.POST['password'])
            print(request.POST['user'])
            print(user)
            if user is not None and user.is_active:
                auth.login(request,user)
                return redirect("/")
            else:
                contexto = {"error" : "error"}
                return render(request,"login.html",contexto)

        else:
            contexto = {"error" : "error"}
            return render(request,"login.html",contexto)
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect("/")

@login_required(login_url='/login')
def vista_logueado(request):
    if request.method == 'POST':
        if ("cerrar" in request.POST.keys()):
            auth.logout(request)
            return redirect("/")
    return render(request,"logueado.html")

def newJuguete(request):
    if request.method == "POST":
        form = JugueteForm(request.POST or None)
        if form.is_valid():
            form.save()
        if ("nombre" in request.POST.keys()) and ("precio" in request.POST.keys()) and ("cantidad" in request.POST.keys()) and ("descripcion" in request.POST.keys()):
            juguete=Juguete()
            juguete.nombre=request.POST["nombre"]
            juguete.precio=request.POST["precio"]
            juguete.cantidad=request.POST["cantidad"]
            juguete.descripcion=request.POST["descripcion"]
            juguete.save()
        if ("cerrar" in request.POST.keys()):
            auth.logout(request)
            return redirect("/login/")
    form = JugueteForm(request.POST or None)
    contexto = {"usuario":request.user,"form":form}
    return render(request,"newJuguete.html",contexto)

def newToy(request):
    if request.method == "POST":
        form = JugueteForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
        if ("nombre" in request.POST.keys()) and ("precio" in request.POST.keys()) and ("cantidad" in request.POST.keys()) and ("descripcion" in request.POST.keys()  and ("imageFile" in request.POST.keys())):
            juguete=Juguete()
            juguete.nombre      =request.POST["nombre"]
            juguete.precio      =request.POST["precio"]
            juguete.cantidad    =request.POST["cantidad"]
            juguete.descripcion =request.POST["descripcion"]
            juguete.imageFile   =request.POST["imageFile"]
            juguete.save()
    else:
        form = JugueteForm(request.POST or None)
    contexto = {"usuario":request.user,"form":form}
    return render(request,"newToy.html",contexto)



def showImage(request):
    lastImage = Image.objects.last()
    print(lastImage)
    imageFile = lastImage.imageFile
    print(imageFile)
    form = ImageForm(request.POST or None, request.FILES or None)
  
    contexto = {"usuario":request.user,"form":form}
    return render(request,"newJuguete.html",contexto)
    
    context = {'imageFile': imageFile,
               'form': form}
    
    return render(request,'images.html',context)