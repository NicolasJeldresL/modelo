from django.contrib import admin
from .models import Direccion, Curso, Profesor, Estudiante

admin.site.register(Direccion)
admin.site.register(Curso)
admin.site.register(Profesor)
admin.site.register(Estudiante)