from django import forms


class Deporte_formulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    grupo = forms.IntegerField()

class Estudiante_formulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    nombre_deporte = forms.CharField(max_length=30)

class Profesor_formulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=30)