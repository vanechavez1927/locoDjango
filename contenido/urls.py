from django.urls import path

from django.conf import settings
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cursos', views.cursos, name='cursos'),
    path('contacto', views.contacto, name='contacto'),
    path('registros', views.registros, name='registros'),
    path('cursos/editar/<int:id>/', views.editar_curso, name='editar_curso'),
    path('cursos/eliminar/<int:id>/', views.eliminar_curso, name='eliminar_curso'),
]