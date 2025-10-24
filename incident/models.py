from django.db import models
from users.models import User
from risk.models import Risk


class Incident(models.Model):
    """Registro de incidentes o eventos de seguridad"""

    SEVERITY_CHOICES = [
        (1, "Baja"),
        (2, "Media"),
        (3, "Alta"),
        (4, "Crítica"),
    ]

    STATUS_CHOICES = [  # ✅ Agrega esto
        ("OPEN", "Abierto"),
        ("IN_PROGRESS", "En progreso"),
        ("RESOLVED", "Resuelto"),
    ]

    title = models.CharField(max_length=200, verbose_name="Título del incidente")
    description = models.TextField(verbose_name="Descripción")
    severity = models.IntegerField(choices=SEVERITY_CHOICES, default=2)
    date_detected = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha detectado"
    )

    related_risk = models.ForeignKey(
        Risk,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="incidents",
        verbose_name="Riesgo relacionado",
    )

    handled_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="handled_incidents",
        verbose_name="Atendido por",
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="OPEN",
        verbose_name="Estado",
    )

    class Meta:
        verbose_name = "Incidente"
        verbose_name_plural = "Incidentes"
        ordering = ["-date_detected"]

    def __str__(self):
        status_display = dict(self.STATUS_CHOICES).get(self.status, self.status)
        return f"{self.title} ({status_display})"
