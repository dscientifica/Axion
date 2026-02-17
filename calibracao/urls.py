from django.urls import path
from .views import pdf_calibracao, instrumento_snapshot

urlpatterns = [
    path(
        "pdf/<int:calibracao_id>/",
        pdf_calibracao,
        name="pdf_calibracao",
    ),
    path(
        "api/instrumento/<uuid:instrumento_id>/",
        instrumento_snapshot,
        name="instrumento_snapshot",
    ),
]

