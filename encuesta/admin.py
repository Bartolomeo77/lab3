from django.contrib import admin

from encuesta.models import Pregunta, Opcion
# Register your models here.

admin.site.register(Pregunta)
admin.site.register(Opcion)
