from django import forms 
from cursos.models import Curso

class Cursos(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'descripcion', 'duracion', 'precio', 'maximo', 'gratis', 'imagen']