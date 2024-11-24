from django.shortcuts import render,redirect
from . import models
from .formularios import formaddest

# Create your views here.
def index(request):
    est = models.Estudiantes.objects.all()
    mat = models.Materias.objects.all()
    return render(request, 'index.html',
                  {'est':est},{'mat':mat})

def formest(request):
    form = formaddest.FormEst()
    form2 = formaddest.FormMat()
    return render(request, 'formulario.html',
                  {'form':form},{'form2':form2})

def gestud(request):
    
    #INSERT INTO Table VALUES ? ? ? ?
    models.Estudiantes.objects.create(
        nombre = request.POST.get('nom'),
        carnet = request.POST.get('carn'),
        edad = request.POST.get('ed'),
        curso = request.POST.get('cur'),
    )
    return redirect('/')

def agrest(request):
    form2 = formaddest.FormMat()
    return render(request,'formaddest.html',
                  {'form2':form2})

def borrest(request,id):
    estudiante = models.Estudiantes.objects.get(id=id)
    estudiante.delete()
    return redirect('/')