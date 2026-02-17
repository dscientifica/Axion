# anexos/models.py
import uuid
from django.db import models

class Anexo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    arquivo = models.FileField(upload_to="anexos/")
    descricao = models.CharField(max_length=255, blank=True)

    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Anexo"
        verbose_name_plural = "Anexos"

    def __str__(self):
        return self.descricao or self.arquivo.name

