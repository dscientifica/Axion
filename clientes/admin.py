from django.contrib import admin
from .models import Cliente, ContatoCliente


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):

    list_display = (
        "razao_social",
        "nome_empresa",
        "cnpj",
        "ativo",
        "created_at",
    )

    search_fields = (
        "razao_social",
        "nome_empresa",
        "cnpj",
    )

    list_filter = (
        "ativo",
    )

    ordering = ("razao_social",)



@admin.register(ContatoCliente)
class ContatoClienteAdmin(admin.ModelAdmin):
    list_display = (
        "nome",
        "cliente",
        "email",
        "telefone",
        "principal",
    )

    list_filter = ("principal",)

