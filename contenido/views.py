from django.shortcuts import get_object_or_404, redirect, render
from .forms import Cursos
from cursos.models import Curso
# Create your views here.

def inicio(request):
    return render(request, "inicio.html")

def cursos(request):
    cursos = Curso.objects.all()
    return render(request, "cursos.html", {'cursos':cursos})

def contacto(request):
    return render(request, "contacto.html")

def registros(request):
    if request.method=='POST':
        form= Cursos(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'registros.html')
    form = Cursos()
    return render(request, "registros.html", {'form':form})


def editar_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    if request.method == 'POST':
        form = Cursos(request.POST, request.FILES, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('cursos')
    else:
        form = Cursos(instance=curso)
    return render(request, 'editar_curso.html', {'form': form})

def eliminar_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    curso.delete()
    return redirect('cursos')