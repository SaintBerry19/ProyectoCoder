from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import *

def curso(request):
    curso=Curso(nombre="Desarrollo Web",camada= 19854)
    curso.save()
    documento= f"---->Curso : {curso.nombre} Camada: {curso.camada}"
    return HttpResponse(documento)

def Inicio(request):
    return render (request, "AppCoder/Inicio.html")

def Curso(request):
    return render (request, "AppCoder/Curso.html")

def Profesor(request):
    return render (request, "AppCoder/Profesor.html")

def Estudiante(request):
    return render (request, "AppCoder/Estudiante.html")

def Entregable(request):
    return render (request, "AppCoder/Entregable.html")

