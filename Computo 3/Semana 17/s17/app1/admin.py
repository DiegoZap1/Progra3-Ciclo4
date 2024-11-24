from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Estudiantes)
admin.site.register(models.Materias)

'''@admin.register(models.Estudiantes)
@admin.register(models.Materias)
class EstAdmin(admin.ModelAdmin):
    pass
class EstMaterias(admin.ModelAdmin):
    pass'''