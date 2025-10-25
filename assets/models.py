from django.db import models
from django.conf import settings


class Asset(models.Model):
    """
    Representa un activo de la organización que puede estar vinculado a uno o varios riesgos.
    """

    ASSET_TYPE_CHOICES = [
        ("HARDWARE", "Hardware"),
        ("SOFTWARE", "Software"),
        ("NETWORK", "Red / Comunicaciones"),
        ("DATA", "Datos / Información"),
        ("SERVICE", "Servicio"),
        ("OTHER", "Otro"),
    ]

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    asset_type = models.CharField(max_length=20, choices=ASSET_TYPE_CHOICES)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="owned_assets",
    )
    criticality = models.IntegerField(
        choices=[
            (1, "Baja"),
            (2, "Media"),
            (3, "Alta"),
            (4, "Crítica"),
        ],
        default=2,
        help_text="Nivel de importancia del activo para la organización.",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.get_asset_type_display()})"
