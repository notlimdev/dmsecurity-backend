from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import User


class Risk(models.Model):
    """Modelo de Riesgo para análisis de seguridad"""

    # Estados posibles del riesgo
    STATUS_CHOICES = [
        ("IDENTIFIED", "Identificado"),
        ("IN_TREATMENT", "En Tratamiento"),
        ("MITIGATED", "Mitigado"),
        ("CLOSED", "Cerrado"),
    ]

    # Información básica
    title = models.CharField(max_length=200, verbose_name="Título del riesgo")
    description = models.TextField(verbose_name="Descripción")

    # Evaluación del riesgo (1 a 5)
    likelihood = models.IntegerField(
        verbose_name="Probabilidad",
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="1=Muy improbable, 5=Muy probable",
    )
    impact = models.IntegerField(
        verbose_name="Impacto",
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="1=Insignificante, 5=Catastrófico",
    )

    # Gestión
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="IDENTIFIED",
        verbose_name="Estado",
    )

    identified_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="identified_risks",
        verbose_name="Identificado por",
    )

    # Fechas
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Última actualización"
    )

    class Meta:
        verbose_name = "Riesgo"
        verbose_name_plural = "Riesgos"
        ordering = ["-created_at"]  # Más recientes primero

    @property
    def risk_level(self):
        """Calcula el nivel de riesgo: Probabilidad × Impacto"""
        return self.likelihood * self.impact

    @property
    def risk_level_name(self):
        """Retorna el nombre del nivel de riesgo"""
        level = self.risk_level
        if level <= 5:
            return "Bajo"
        elif level <= 12:
            return "Medio"
        elif level <= 20:
            return "Alto"
        else:
            return "Crítico"

    def __str__(self):
        return f"{self.title} - {self.risk_level_name} ({self.risk_level})"

