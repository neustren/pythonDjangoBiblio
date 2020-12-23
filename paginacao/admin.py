from django.contrib import admin

# Register your models here.
from .models import Materia


@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco')
