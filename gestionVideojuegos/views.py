from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context
from .models import videojuegos
from datetime import datetime
# Create your views here.
def saludo(request): #primera vista
    nombre="Julio"
    apellido="Diaz"

    plant_externa=open('C:/Users/PERSONAL/Documents/ProyectosDJANGO/prueba/plantillas/plantillas.html')
    plntll=Template(plant_externa.read())
    plant_externa.close
    ctx=Context({"nomb_person":nombre,"ape_person":apellido})
    plantilla=plntll.render(ctx)


    return HttpResponse(plantilla)

def inicio(request):
    lista_videojuegos = videojuegos.objects.all()
    fecha_actual = datetime.now()
    return render(request, 'inicio.html',{'videojuegos': lista_videojuegos, 'fecha_actual': fecha_actual})
def mision(request):
    return render(request, 'mision.html')

def vision(request):
    return render(request, 'vision.html')

def acerca_de(request):
    return render(request, 'acerca_de.html')