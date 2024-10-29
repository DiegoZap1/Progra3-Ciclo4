from django.shortcuts import render
from django.http.response import HttpResponse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView

def home(request):
    return HttpResponse(render, 'home.html')

def gcamisas(request):
    return HttpResponse(render,'camisas.html')

def view1(request):
    return HttpResponse('View basada en funciones')

def formpost(request):
    return HttpResponse('Aqui va un form')

def formget(request):
    return HttpResponse('POST on click')

class view2(LoginRequiredMixin,TemplateView):
    template_name = 'ejemplo.html'
    '''def get(self,request):
        return HttpResponse('View basada en clases')'''
    
@login_required
class view3(View):
    def get(self,request):
        return render(request,'form.html')

    def post(self,request):
        HttpResponse('POST de clases')
