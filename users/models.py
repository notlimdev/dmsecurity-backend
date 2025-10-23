from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Modelo personalizado de usuario con roles."""

    ROLE_CHOICES = [
        ("ADMIN", "Administrador"),
        ("ANALISTA", "Analista"),
        ("AUDITOR", "Auditor"),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="ANALISTA",
        verbose_name="Rol del usuario",
    )
    phone = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="Teléfono"
    )
    organization = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Organización"
    )

    @property
    def role_display(self) -> str:
        """Devuelve el nombre legible del rol."""
        role_map = dict(self.ROLE_CHOICES)
        role_value = (
            str(self.role) if isinstance(self.role, (str, bytes)) else ""
        )  # ✅ tipado explícito
        return role_map.get(role_value, "Desconocido")

    def __str__(self) -> str:
        return f"{self.username} ({self.role_display})"
