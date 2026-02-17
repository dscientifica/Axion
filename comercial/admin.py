from django.contrib import admin
from .models import Proposta


@admin.register(Proposta)
class PropostaAdmin(admin.ModelAdmin):
    list_display = ("id", "cliente", "valor", "status", "data_criacao")
    list_filter = ("status",)

