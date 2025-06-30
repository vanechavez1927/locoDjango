from django.contrib import admin
from .models import Curso
from django.utils.html import format_html 

class AdministrarCurso(admin.ModelAdmin):
    list_display = (
        'nombre',
        'categoria',
        'duracion_horas',
        'precio',
        'activo',
        'fecha_creacion',
    )
    ordering = ('fecha_creacion',)
    search_fields = ('nombre', 'descripcion', 'categoria')
    date_hierarchy = 'fecha_creacion'
    list_filter = ('activo', 'categoria', 'precio')

admin.site.register(Curso, AdministrarCurso)

