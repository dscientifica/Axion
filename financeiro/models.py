import uuid
from django.db import models
from django.utils import timezone
from clientes.models import Cliente


# =========================
# CATEGORIA FINANCEIRA
# =========================
class CategoriaFinanceira(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Categoria Financeira"
        verbose_name_plural = "Categorias Financeiras"
        ordering = ("nome",)

    def __str__(self):
        return self.nome


# =========================
# CONTAS A PAGAR
# =========================
class ContaPagar(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    descricao = models.CharField(max_length=200)
    fornecedor = models.CharField(max_length=200)

    categoria = models.ForeignKey(
        CategoriaFinanceira,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="contas_pagar"
    )

    valor = models.DecimalField(max_digits=12, decimal_places=2)
    vencimento = models.DateField()
    data_pagamento = models.DateField(null=True, blank=True)

    comprovante = models.FileField(
        upload_to="financeiro/contas_pagar/",
        null=True,
        blank=True
    )

    STATUS_CHOICES = [
        ("pendente", "Pendente"),
        ("pago", "Pago"),
        ("atrasado", "Atrasado"),
        ("cancelado", "Cancelado"),
    ]

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="pendente"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Conta a Pagar"
        verbose_name_plural = "Contas a Pagar"
        ordering = ("vencimento",)

    def save(self, *args, **kwargs):
        if self.status not in ("pago", "cancelado") and self.vencimento < timezone.now().date():
            self.status = "atrasado"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.descricao} - {self.fornecedor}"


# =========================
# CONTAS A RECEBER
# =========================
class ContaReceber(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
        related_name="contas_receber"
    )

    descricao = models.CharField(max_length=200)

    valor = models.DecimalField(max_digits=12, decimal_places=2)
    vencimento = models.DateField()
    data_recebimento = models.DateField(null=True, blank=True)

    comprovante = models.FileField(
        upload_to="financeiro/contas_receber/",
        null=True,
        blank=True
    )

    STATUS_CHOICES = [
        ("pendente", "Pendente"),
        ("recebido", "Recebido"),
        ("atrasado", "Atrasado"),
        ("cancelado", "Cancelado"),
    ]

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="pendente"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Conta a Receber"
        verbose_name_plural = "Contas a Receber"
        ordering = ("vencimento",)

    def save(self, *args, **kwargs):
        if self.status not in ("recebido", "cancelado") and self.vencimento < timezone.now().date():
            self.status = "atrasado"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.cliente.razao_social} - R$ {self.valor}"


# =========================
# IMPOSTOS
# =========================
class Imposto(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    nome = models.CharField(max_length=100)

    competencia = models.CharField(
        max_length=7,
        help_text="Formato MM/AAAA (ex: 01/2026)"
    )

    valor = models.DecimalField(max_digits=12, decimal_places=2)
    vencimento = models.DateField()

    comprovante = models.FileField(
        upload_to="financeiro/impostos/",
        null=True,
        blank=True
    )

    pago = models.BooleanField(default=False)
    data_pagamento = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Imposto"
        verbose_name_plural = "Impostos"
        ordering = ("-vencimento",)

    def __str__(self):
        return f"{self.nome} - {self.competencia}"

