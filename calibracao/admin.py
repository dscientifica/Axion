from datetime import date
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import (
    Instrumento,
    InstrumentoTecnico,
    Documento,
    OrdemServico,
    Padrao,
    Periodicidade,
    Calibracao,
)

# =========================
# INLINES
# =========================

class PeriodicidadeInline(admin.TabularInline):
    model = Periodicidade
    extra = 1


class InstrumentoTecnicoInline(admin.StackedInline):
    model = InstrumentoTecnico
    extra = 0


# =========================
# INSTRUMENTO
# =========================

@admin.register(Instrumento)
class InstrumentoAdmin(admin.ModelAdmin):
    list_display = (
        "codigo",
        "descricao",
        "marca",
        "modelo",
        "tipo",
        "cliente",
        "status",
    )

    search_fields = (
        "codigo",
        "descricao",
        "marca",
        "modelo",
        "numero_serie",
        "cliente__razao_social",
    )

    list_filter = (
        "status",
        "cliente",
    )

    autocomplete_fields = ("cliente",)
    ordering = ("descricao",)

    inlines = [
        InstrumentoTecnicoInline,
        PeriodicidadeInline,
    ]


# =========================
# CALIBRAÇÃO
# =========================

@admin.register(Calibracao)
class CalibracaoAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "instrumento",
        "data_calibracao",
        "validade",
        "periodicidade_status",
        "status",
        "gerar_pdf",
        "arquivo_link",
    )

    readonly_fields = (
        "descricao",
        "marca",
        "modelo",
        "tipo",
        "numero_serie",
        "gerar_pdf",
    )

    fieldsets = (
        ("Instrumento", {
            "fields": ("instrumento",)
        }),
        ("Identificação do Instrumento (snapshot)", {
            "fields": (
                "descricao",
                "marca",
                "modelo",
                "tipo",
                "numero_serie",
                "gerar_pdf",
            )
        }),
        ("Dados Operacionais", {
            "fields": (
                "os_cliente",
                "instrumento_critico",
                "condicao_uso",
                "empresa",
                "local_instalacao",
                "local_armazenamento",
                "sub_local",
            )
        }),
        ("Calibração", {
            "fields": (
                "data_calibracao",
                "validade",
                "certificado",
                "status",
                "observacoes",
            )
        }),
    )

    def save_model(self, request, obj, form, change):
        instrumento = obj.instrumento

        if instrumento:
            obj.descricao = instrumento.descricao
            obj.marca = instrumento.marca
            obj.modelo = instrumento.modelo
            obj.tipo = instrumento.tipo
            obj.numero_serie = instrumento.numero_serie or ""

        super().save_model(request, obj, form, change)

    def arquivo_link(self, obj):
        if obj.certificado:
            return format_html(
                '<a href="{}" target="_blank">📄 Abrir</a>',
                obj.certificado.url
            )
        return "-"

    arquivo_link.short_description = "Certificado"

    def gerar_pdf(self, obj):
        if not obj.pk:
            return "-"
        url = reverse("pdf_calibracao", args=[obj.id])
        return format_html(
            '<a class="button" href="{}" target="_blank">Gerar PDF</a>',
            url
        )

    gerar_pdf.short_description = "PDF"

    def periodicidade_status(self, obj):
        if not obj.validade:
            return "-"
        return "🟢 Adequado ao uso" if obj.validade >= date.today() else "🔴 Vencido"

    periodicidade_status.short_description = "Periodicidade"


# =========================
# DOCUMENTOS
# =========================

@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = (
        "codigo",
        "titulo",
        "norma",
        "tipo_documento",
        "grupo",
        "data_cadastro",
        "arquivo_link",
    )

    list_filter = ("tipo_documento", "grupo")

    search_fields = (
        "codigo",
        "titulo",
        "norma",
    )

    fields = (
        "codigo",
        "titulo",
        "tipo_documento",
        "norma",
        "grupo",
        "arquivo",
    )

    def arquivo_link(self, obj):
        if obj.arquivo:
            return format_html(
                '<a href="{}" target="_blank">📄 Abrir</a>',
                obj.arquivo.url
            )
        return "-"

    arquivo_link.short_description = "Arquivo"


# =========================
# ORDEM DE SERVIÇO
# =========================

@admin.register(OrdemServico)
class OrdemServicoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "cliente",
        "data_abertura",
    )

    autocomplete_fields = ("cliente",)


# =========================
# PADRÕES
# =========================

@admin.register(Padrao)
class PadraoAdmin(admin.ModelAdmin):
    list_display = (
        "codigo",
        "descricao",
        "status",
        "vencimento",
        "certificado_link",
    )

    list_filter = ("status",)

    search_fields = (
        "codigo",
        "descricao",
    )

    fields = (
        "codigo",
        "descricao",
        "status",
        "vencimento",
        "certificado",
    )

    def certificado_link(self, obj):
        if obj.certificado:
            return format_html(
                '<a href="{}" target="_blank">📄 Abrir</a>',
                obj.certificado.url
            )
        return "-"

    certificado_link.short_description = "Certificado"

