from django.urls import path

from django.conf import settings
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cursos', views.cursos, name='cursos'),
     path('contacto', views.contacto, name='contacto'),
]