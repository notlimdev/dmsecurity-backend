from rest_framework import serializers
from .models import Risk
from security.models import Security  # 👈 Importa el modelo Security


class RiskSerializer(serializers.ModelSerializer):
    """Serializador para el modelo Risk"""

    # Campos calculados (solo lectura)
    risk_level = serializers.IntegerField(read_only=True)
    risk_level_name = serializers.CharField(read_only=True)

    # Mostrar el nombre del usuario que identificó el riesgo
    identified_by_name = serializers.CharField(
        source="identified_by.username", read_only=True
    )

    # 👇 Nuevo campo: lista de IDs de controles asociados
    controls = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Security.objects.all(), required=False
    )

    class Meta:
        model = Risk
        fields = [
            "id",
            "title",
            "description",
            "likelihood",
            "impact",
            "risk_level",
            "risk_level_name",
            "status",
            "identified_by",
            "identified_by_name",
            "controls",  # 👈 Agrégalo aquí también
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
