from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import Curso, Profesor
from AppCoder.forms import CursoFormulario, ProfesorFormulario 

# Create your views here.

def curso(request):

      curso =  Curso(nombre="Desarrollo web", camada="19881")
      curso.save()
      documentoDeTexto = f"--->Curso: {curso.nombre}   Camada: {curso.camada}"


      return HttpResponse(documentoDeTexto)


def inicio(request):

      return render(request, "AppCoder/inicio.html")

def cursos(request):
      if request.method == 'POST':
            miFormulario= CursoFormulario(request.POST)
            print (miFormulario)
            if miFormulario.is_valid:
                  informacion =miFormulario.cleaned_data
                  curso= Curso(nombre=informacion['curso'], camada=informacion['camada'])
                  curso.save()
            return render(request,'AppCoder/inicio.html')
      else:
            miFormulario=CursoFormulario()
      return render (request, 'AppCoder/CursoFormulario.html', {"miFormulario":miFormulario})

def profesores(request):
      if request.method == "POST":
            miFormulario= ProfesorFormulario(request.POST)
            print (miFormulario)
            if miFormulario.is_valid:
                  informacion =miFormulario.cleaned_data
                  profesor= Profesor(nombre=informacion['nombre'], apellido=informacion['apellido'],email=informacion['email'], profesion=informacion['profesion'])
                  profesor.save()
            return render(request,'AppCoder/inicio.html')
      else:
            miFormulario=ProfesorFormulario()
      return render (request, 'AppCoder/ProfesorFormulario.html', {"miFormulario":miFormulario})


def estudiantes(request):

      return render(request, "AppCoder/estudiantes.html")


def entregables(request):

      return render(request, "AppCoder/entregables.html")

# def cursoFormulario(request):
#       if request.method == 'POST':
#             miFormulario= CursoFormulario(request.POST)
#             print (miFormulario)
#             if miFormulario.is_valid:
#                   informacion =miFormulario.cleaned_data
#                   curso= Curso(nombre=informacion['curso'], camada=informacion['camada'])
#                   curso.save()
#             return render(request,'AppCoder/inicio.html')
#       else:
#             miFormulario=CursoFormulario()
#       return render (request, 'AppCoder/CursoFormulario.html', {"miFormulario":miFormulario})


# def profesorFormulario(request):
#       if request.method == "POST":
#             miFormulario= ProfesorFormulario(request.POST)
#             print (miFormulario)
#             if miFormulario.is_valid:
#                   informacion =miFormulario.cleaned_data
#                   profesor= Profesor(nombre=informacion['nombre'], apellido=informacion['apellido'],email=informacion['email'], profesion=informacion['profesion'])
#                   profesor.save()
#             return render(request,'AppCoder/inicio.html')
#       else:
#             miFormulario=ProfesorFormulario()
#       return render (request, 'AppCoder/ProfesorFormulario.html', {"miFormulario":miFormulario})


def busquedaCamada(request):
      return render (request, "AppCoder/busquedaCamada.html")

def buscar (request):
      if request.GET["camada"]:
            camada=request.GET['camada']
            cursos= Curso.objects.filter(camada__icontains=camada)
            return render (request, "AppCoder/resultadosBusqueda.html",{"cursos":cursos, "camada":camada})
      else:
            respuesta="No enviaste datos"
      # respuesta = f"Estoy buscando la camada numero: {request.GET['camada']}"
      # return HttpResponse(respuesta)
      return render(request,"AppCoder/inicio.html",{"respuesta":respuesta})