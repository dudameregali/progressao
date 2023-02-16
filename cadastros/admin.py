from django.contrib import admin

from .models import Consulta, Paciente
# Register your models here.

admin.site.register(Paciente)
admin.site.register(Consulta)