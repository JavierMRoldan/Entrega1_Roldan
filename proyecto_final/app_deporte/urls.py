from django.urls import path
from . import views


urlpatterns = [

    path('', views.inicio, name='inicio'),
    path('deportes/', views.deportes, name='deportes'),
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('profesores/', views.profesores, name='profesores'),

    path('alta_formularios', views.alta_formularios, name='alta_formularios'),
    path('alta_deporte', views.deporte_formularios, name='alta_deporte'),
    path('alta_estudiante', views.estudiante_formularios, name='alta_estudiante'),
    path('alta_profesor', views.profesor_formularios, name='alta_profesor'),

    path('buscar_formularios', views.buscar_formularios, name='buscar_formularios'),
    #--------------------
    path('buscar_deporte', views.buscar_deporte, name='buscar_deporte'),
    path('buscar_estudiante', views.buscar_estudiante, name='buscar_estudiante'),
    path('buscar_profesor', views.buscar_profesor, name='buscar_profesor'),
    #--------------------
    path('buscador_deporte', views.buscador_deporte),
    path('buscador_estudiante', views.buscador_estudiante),
    path('buscador_profesor', views.buscador_profesor),

]