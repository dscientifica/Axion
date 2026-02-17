import uuid
from django.db import models
from clientes.models import Cliente


# =========================
# PROPOSTA COMERCIAL
# =========================
class Proposta(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    STATUS_CHOICES = (
        ("rascunho", "Rascunho"),
        ("enviada", "Enviada"),
        ("aprovada", "Aprovada"),
        ("recusada", "Recusada"),
    )

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
        related_name="propostas"
    )

    descricao = models.CharField(max_length=255)

    valor = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="rascunho"
    )

    data_criacao = models.DateTimeField(auto_now_add=True)
    validade = models.DateField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Proposta Comercial"
        verbose_name_plural = "Propostas Comerciais"
        ordering = ("-data_criacao",)

    def __str__(self):
        return f"Proposta {self.id} - {self.cliente.razao_social}"

