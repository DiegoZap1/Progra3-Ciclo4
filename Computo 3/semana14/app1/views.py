from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Mi primera pagina de DJango')

def home(request):
    return render(request,'inicio.html')