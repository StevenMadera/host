import uuid
from django.shortcuts import render, redirect
from .models import Receta
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect


# Create your views here.

def home(request):
    recetasListadas = Receta.objects.all()
    return render(request, "gestionRecetas.html", {"recetas": recetasListadas})

def index(request):
    index = Receta.objects.all()
    return render(request, "index.html", {"recetas": index})

def receta(request, id):
    receta = Receta.objects.get(id=id)
    return render(request, "receta.html", {"receta": receta})

def gestionRecetas(request):
    gestionRecetas = Receta.objects.all()
    return render(request, "gestionRecetas.html", {"recetas": gestionRecetas})

def base(request):
    base = Receta.objects.all()
    return render(request, "base.html", {"base": base})

def registrarReceta(request):
    nombre_receta = request.POST['txtnombre_receta']
    calificacion = request.POST['numcalificacion']
    imagen = request.FILES.get('txtImagen')
    
    receta = Receta.objects.create(nombre_receta=nombre_receta, calificacion=calificacion, imagen=imagen)
    messages.success(request, 'Receta agregada')
    return redirect('/')

def editarReceta(request, id):
    receta = Receta.objects.get(id=id)
    return render(request, "editarReceta.html", {"receta": receta})

def edicionReceta(request):
    id = request.POST['txtid']
    nombre_receta = request.POST['txtnombre_receta']
    calificacion = request.POST['numcalificacion']
    imagen = request.FILES.get('txtImagen')

    receta = Receta.objects.get(id=id)
    receta.id = id
    receta.nombre_receta = nombre_receta
    receta.calificacion = calificacion
    if imagen:
     receta.imagen = imagen
    receta.save()
    messages.info(request, 'Receta editada')

    return redirect('/')

def eliminarReceta(request, id):
    receta = Receta.objects.get(id=id)
    receta.delete()
    messages.error(request, 'Receta eliminada')

    return redirect('/')
    
def buscarReceta(request):
    if request.method == 'GET':
        textoBusqueda = request.GET['txtBuscar']
        recetas = Receta.objects.filter(Q(nombre_receta__icontains=textoBusqueda))
        return render(request, 'gestionRecetas.html', {'recetas': recetas})
    else:
        return render(request, 'gestionRecetas.html')