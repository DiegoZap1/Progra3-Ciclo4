from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('formest',views.formest),
    path('add/', views.gestud),
    path('add2/',views.agrest),
    path('borrar/',views.borrest),
]