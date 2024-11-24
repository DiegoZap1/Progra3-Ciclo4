from django import forms
from app1 import models

class FormEst(forms.Form):
    nom = forms.CharField(max_length=100,label="Nombre")
    carn = forms.CharField(max_length=100,label="Carnet")
    ed = forms.IntegerField(label="Edad")
    cur = forms.CharField(max_length=100,label="Curso")

class FormMat(forms.Form):
    nombre = forms.CharField(max_length=100)
    estds = forms.ModelMultipleChoiceField(
        queryset = models.Materias.objects.all(),
        widget = forms.CheckboxSelectMultiple,
        required = False,
    )

    class Meta:
        model = models.Estudiantes
        fields = ['nombre','carnet','edad','curso']