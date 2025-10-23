from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import User


class Security(models.Model):
    """Registro de medidas o controles de seguridad aplicados"""

    CONTROL_TYPE_CHOICES = [
        ("PREVENTIVE", "Preventivo"),
        ("DETECTIVE", "Detectivo"),
        ("CORRECTIVE", "Correctivo"),
    ]

    STATUS_CHOICES = [
        ("ACTIVE", "Activo"),
        ("INACTIVE", "Inactivo"),
        ("UNDER_REVIEW", "En revisión"),
    ]

    # Información básica
    name = models.CharField(max_length=200, verbose_name="Nombre del control")
    description = models.TextField(verbose_name="Descripción")

    # Clasificación del control
    control_type = models.CharField(
        max_length=20,
        choices=CONTROL_TYPE_CHOICES,
        default="PREVENTIVE",
        verbose_name="Tipo de control",
    )

    effectiveness = models.IntegerField(
        verbose_name="Efectividad",
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="1=Muy baja, 5=Muy alta",
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="ACTIVE",
        verbose_name="Estado del control",
    )

    implemented_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="implemented_controls",
        verbose_name="Implementado por",
    )

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Última actualización"
    )

    class Meta:
        verbose_name = "Control de Seguridad"
        verbose_name_plural = "Controles de Seguridad"
        ordering = ["-created_at"]

    def __str__(self):
        status_display = dict(self.STATUS_CHOICES).get(self.status, self.status)
        return f"{self.name} ({status_display})"

