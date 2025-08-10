from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

class Curso(models.Model):
    nombre = models.CharField("Nombre del curso", max_length=255)
    descripcion = models.TextField("Descripción", default="Sin descripción")
    duracion = models.IntegerField("Duración (minutos)", default=60)  
    precio = models.DecimalField("Precio", max_digits=8, decimal_places=2, default=0.00)
    maximo = models.IntegerField("Cupo máximo", default=0) 
    gratis = models.BooleanField("¿Es gratuito?", default=False)
    imagen = models.ImageField("Imagen del curso", null=True, upload_to='fotos')
    fecha_creacion = models.DateTimeField("Fecha de creación", auto_now_add=True)
    fecha_final = models.DateTimeField("Última actualización",  default=timezone.now)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['fecha_creacion']

    def __str__(self):
        return self.nombre


class Actividad(models.Model):
    id_actividad = models.AutoField(primary_key=True, verbose_name="Clave de Actividad")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso Relacionado")
    nombre_actividad = models.CharField(max_length=150, verbose_name="Nombre de la Actividad")
    descripcion_Actividad = RichTextField(verbose_name="Comentario", default="Nada")
    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha de Creación',
        help_text="Fecha y hora en que se registró el curso. Se genera automáticamente."
    )

    class Meta:
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'
        ordering = ['fecha_creacion']

    def __str__(self):
        return self.nombre_actividad