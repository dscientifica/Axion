import uuid
from django.db import models


class Cliente(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    razao_social = models.CharField(max_length=255)
    nome_empresa = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, unique=True)

    ativo = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("razao_social",)

    def __str__(self):
        return f"{self.razao_social} ({self.cnpj})"


class ContatoCliente(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name="contatos"
    )

    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    telefone = models.CharField(max_length=20, blank=True)
    principal = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Contato do Cliente"
        verbose_name_plural = "Contatos do Cliente"
        ordering = ("-principal", "nome")

    def __str__(self):
        return f"{self.nome} — {self.cliente.razao_social}"


