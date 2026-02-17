import uuid
from django.db import models
from clientes.models import Cliente
from anexos.models import Anexo

# =========================
# INSTRUMENTO
# =========================

class Instrumento(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    STATUS_CHOICES = (
        ("ativo", "Ativo"),
        ("inativo", "Inativo"),
        ("manutencao", "Em Manutenção"),
    )

    codigo = models.CharField(max_length=50, unique=True)
    descricao = models.CharField(max_length=255)

    marca = models.CharField(max_length=100, blank=True)
    modelo = models.CharField(max_length=100, blank=True)
    tipo = models.CharField(max_length=100, blank=True)

    numero_serie = models.CharField(max_length=100, blank=True, null=True)

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
        related_name="instrumentos"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="ativo"
    )

    proxima_calibracao = models.DateField(blank=True, null=True)
    ativo = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.codigo} - {self.descricao}"


# no mesmo arquivo models.py

class InstrumentoTecnico(models.Model):
    instrumento = models.OneToOneField(
        Instrumento,
        on_delete=models.CASCADE,
        related_name="tecnico"
    )

    faixa_medicao = models.CharField(max_length=100, blank=True)
    unidade = models.CharField(max_length=50, blank=True)
    classe = models.CharField(max_length=50, blank=True)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"Técnico - {self.instrumento.codigo}"


# =========================
# DOCUMENTO
# =========================
class Documento(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    TIPO_DOCUMENTO_CHOICES = (
        ("procedimento", "Procedimento"),
        ("instrucao", "Instrução"),
        ("registro", "Registro"),
    )

    titulo = models.CharField(max_length=255)
    codigo = models.CharField(max_length=50, unique=True)

    norma = models.CharField(max_length=100)
    grupo = models.CharField(max_length=100)

    tipo_documento = models.CharField(
        max_length=20,
        choices=TIPO_DOCUMENTO_CHOICES
    )

    arquivo = models.FileField(
        upload_to="documentos/",
        blank=True,
        null=True,
        verbose_name="Arquivo do Documento"
    )

    data_cadastro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo


# =========================
# ORDEM DE SERVIÇO
# =========================
class OrdemServico(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
        related_name="ordens_servico"
    )

    data_abertura = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"OS {self.id} - {self.cliente.razao_social}"


# =========================
# PADRÃO
# =========================
class Padrao(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    STATUS_CHOICES = (
        ("valido", "Válido"),
        ("vencido", "Vencido"),
        ("suspenso", "Suspenso"),
    )

    codigo = models.CharField(max_length=50, unique=True)
    descricao = models.CharField(max_length=255)

    certificado = models.FileField(
        upload_to="padroes/certificados/",
        blank=True,
        null=True,
        verbose_name="Certificado do Padrão"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="valido"
    )

    vencimento = models.DateField()

    def __str__(self):
        return f"{self.codigo} - {self.descricao}"

class Periodicidade(models.Model):

    TIPO_CHOICES = (
        ("calibracao", "Calibração"),
        ("manutencao", "Manutenção"),
    )

    instrumento = models.ForeignKey(
        Instrumento,
        on_delete=models.CASCADE,
        related_name="periodicidades"
    )

    tipo = models.CharField(
        max_length=20,
        choices=TIPO_CHOICES
    )

    intervalo_meses = models.PositiveIntegerField(
        help_text="Intervalo em meses"
    )

    def __str__(self):
        return f"{self.instrumento.codigo} - {self.get_tipo_display()}"



from datetime import date
from dateutil.relativedelta import relativedelta

class Calibracao(models.Model):

    instrumento = models.ForeignKey(
        Instrumento,
        on_delete=models.PROTECT,
        related_name="calibracoes"
    )

    # Snapshot do instrumento
    descricao = models.CharField(max_length=255)
    marca = models.CharField(max_length=100, blank=True)
    modelo = models.CharField(max_length=100, blank=True)
    tipo = models.CharField(max_length=100, blank=True)
    numero_serie = models.CharField(max_length=100, blank=True)

    # Dados operacionais
    os_cliente = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="OS do Cliente"
    )

    instrumento_critico = models.BooleanField(
        default=False,
        verbose_name="Instrumento Crítico"
    )

    condicao_uso = models.BooleanField(
        default=True,
        verbose_name="Instrumento em condição de uso"
    )

    empresa = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="Empresa executante"
    )

    local_instalacao = models.CharField(
        max_length=150,
        blank=True
    )

    local_armazenamento = models.CharField(
        max_length=150,
        blank=True
    )

    sub_local = models.CharField(
        max_length=150,
        blank=True
    )

    # Datas
    data_calibracao = models.DateField()
    validade = models.DateField(blank=True, null=True)

    certificado = models.FileField(
        upload_to="calibracoes/certificados/",
        blank=True,
        null=True
    )

    STATUS_CHOICES = (
        ("aberta", "Aberta"),
        ("concluida", "Concluída"),
        ("cancelada", "Cancelada"),
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="aberta"
    )

    observacoes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return f"Calibração {self.id} - {self.instrumento.codigo}"


