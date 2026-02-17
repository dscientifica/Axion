# anexos/admin.py
from django.contrib import admin
from .models import Anexo

@admin.register(Anexo)
class AnexoAdmin(admin.ModelAdmin):
    list_display = ("descricao", "arquivo", "criado_em")

