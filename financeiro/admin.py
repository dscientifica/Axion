from django.contrib import admin
from .models import (
    CategoriaFinanceira,
    ContaPagar,
    ContaReceber,
    Imposto
)


@admin.register(CategoriaFinanceira)
class CategoriaFinanceiraAdmin(admin.ModelAdmin):
    list_display = ("id", "nome")
   

@admin.register(ContaPagar)
class ContaPagarAdmin(admin.ModelAdmin):
    list_display = (
        "descricao",
        "fornecedor",
        "valor",
        "vencimento",
        "status",
    )
    list_filter = ("status", "vencimento", "categoria")
    date_hierarchy = "vencimento"
    ordering = ("vencimento",)


@admin.register(ContaReceber)
class ContaReceberAdmin(admin.ModelAdmin):
    list_display = (
        "cliente",
        "descricao",
        "valor",
        "vencimento",
        "status",
    )
    list_filter = ("status", "vencimento")
    date_hierarchy = "vencimento"
    ordering = ("vencimento",)


@admin.register(Imposto)
class ImpostoAdmin(admin.ModelAdmin):
    list_display = (
        "nome",
        "competencia",
        "valor",
        "vencimento",
        "pago",
    )
    list_filter = ("pago", "competencia")
    date_hierarchy = "vencimento"
