from django.http import HttpResponse
from django.shortcuts import render
from app_deporte.models import Deporte, Estudiante, Profesor
from django.template import loader
from app_deporte.forms import Deporte_formulario, Estudiante_formulario, Profesor_formulario
# Create your views here.


def inicio(request):

    return render(request, "padre.html")

'''--------------------------------------------------------------------------------------------------'''

def deportes(request):
    deportes = Deporte.objects.all()
    dicc = {'deportes' : deportes}
    plantilla = loader.get_template('deportes.html')
    documento = plantilla.render(dicc)
    return HttpResponse( documento )

'''--------------------------------------------------------------------------------------------------'''

def estudiantes(request):
    estudiantes = Estudiante.objects.all()
    dicc = {'estudiantes' : estudiantes}
    plantilla = loader.get_template('estudiantes.html')
    documento = plantilla.render(dicc)
    return HttpResponse( documento )

'''--------------------------------------------------------------------------------------------------'''

def profesores(request):
    profesores = Profesor.objects.all()
    dicc = {'profesores' : profesores}
    plantilla = loader.get_template('profesores.html')
    documento = plantilla.render(dicc)
    return HttpResponse( documento )

'''--------------------------------------------------------------------------------------------------'''

def alta_formularios(request):

    return render(request, 'alta_formularios.html')

'''/////////////////////////'''

def deporte_formularios(request):

    if request.method == "POST":
        
        mi_deporte = Deporte_formulario(request.POST)
        if mi_deporte.is_valid():
            datos_deporte = mi_deporte.cleaned_data
            deporte = Deporte(nombre=datos_deporte['nombre'] , grupo=datos_deporte['grupo'])
            deporte.save()
            return render(request, 'deportes.html')
    
    return render(request, 'alta_deporte.html')

'''/////////////////////////'''

def estudiante_formularios(request):

    if request.method == "POST":
        mi_estudiante = Estudiante_formulario(request.POST)
        if mi_estudiante.is_valid():
            datos_estudiante = mi_estudiante.cleaned_data
            estudiante = Estudiante(nombre=datos_estudiante['nombre'] , apellido=datos_estudiante['apellido'] , nombre_deporte=datos_estudiante['nombre_deporte'])
            estudiante.save()
            return render(request, 'estudiantes.html')
    
    return render(request, 'alta_estudiante.html')

'''/////////////////////////'''

def profesor_formularios(request):

    if request.method == "POST":
        mi_profesor = Profesor_formulario(request.POST)
        if mi_profesor.is_valid():
            datos_profesor = mi_profesor.cleaned_data
            profesor = Profesor(nombre=datos_profesor['nombre'] , apellido=datos_profesor['apellido'] , profesion=datos_profesor['profesion'] ,  email=datos_profesor['email'])
            profesor.save()
            return render(request, 'profesores.html')
    
    return render(request, 'alta_profesor.html')

'''--------------------------------------------------------------------------------------------------'''

def buscar_formularios(request):

    return render(request, 'buscar_formularios.html')

'''/////////////////////////'''

def buscador_deporte(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']
        deportes = Deporte.objects.filter(nombre__icontains = nombre)
        return render(request , 'resultado_deporte.html' , {"deportes":deportes})
    else:
        return HttpResponse("Campo vacio")

def buscador_estudiante(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']
        estudiantes = Estudiante.objects.filter(nombre__icontains = nombre)
        return render(request , 'resultado_estudiante.html' , {"estudiantes":estudiantes})
    else:
        return HttpResponse("Campo vacio")

def buscador_profesor(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']
        profesores = Profesor.objects.filter(nombre__icontains = nombre)
        return render(request , 'resultado_profesor.html' , {"profesores":profesores})
    else:
        return HttpResponse("Campo vacio")

'''/////////////////////////'''

def buscar_deporte(request):

    return render(request, 'buscar_deporte.html')

'''/////////////////////////'''

def buscar_estudiante(request):

    return render(request, 'buscar_estudiante.html')

'''/////////////////////////'''

def buscar_profesor(request):

    return render(request, 'buscar_profesor.html')

'''--------------------------------------------------------------------------------------------------'''