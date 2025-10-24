from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import User
from risk.models import Risk


class MitigationPlan(models.Model):
    """Plan o acción de mitigación asociada a un riesgo"""

    STATUS_CHOICES = [
        ("PENDING", "Pendiente"),
        ("IN_PROGRESS", "En progreso"),
        ("COMPLETED", "Completado"),
    ]

    risk = models.ForeignKey(
        Risk,
        on_delete=models.CASCADE,
        related_name="mitigation_plans",
        verbose_name="Riesgo asociado",
    )

    action = models.CharField(max_length=255, verbose_name="Acción de mitigación")
    responsible = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="mitigation_responsibles",
        verbose_name="Responsable",
    )

    due_date = models.DateField(verbose_name="Fecha límite")
    progress = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name="Progreso (%)",
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING",
        verbose_name="Estado",
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta:
        verbose_name = "Plan de Mitigación"
        verbose_name_plural = "Planes de Mitigación"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.action} ({self.status})"
