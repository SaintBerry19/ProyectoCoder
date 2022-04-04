from django.urls import path
from AppCoder import views


urlpatterns = [
    path('',views.Inicio),
    path('Curso/',views.Curso),
    path('Profesor/',views.Profesor),
    path('Estudiante/',views.Estudiante),
    path('Entregable/',views.Entregable),
]
