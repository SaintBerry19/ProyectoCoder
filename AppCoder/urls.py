from unicodedata import name
from django.urls import path

from AppCoder import views

urlpatterns = [
   
    path('', views.inicio,name='Inicio' ), #esta era nuestra primer view
    path('Cursos', views.cursos, name='Cursos'),
    path('Profesores', views.profesores,name='Profesores'),
    path('Estudiantes', views.estudiantes,name='Estudiantes'),
    path('Entregables', views.entregables,name='Entregables'),
    # path('CursoFormulario', views.cursoFormulario,name='CursoFormulario'),
    # path('ProfesorFormulario', views.profesorFormulario,name='ProfesorFormulario'),
    path('BusquedaCamada', views.busquedaCamada,name='BusquedaCamada'),
    path('Buscar/', views.buscar),
]

