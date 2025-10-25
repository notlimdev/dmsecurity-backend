from rest_framework import viewsets, permissions
from .models import Risk
from .serializers import RiskSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from .ai_services import generate_mitigation_recommendations


class RiskViewSet(viewsets.ModelViewSet):
    """
    API para gestionar riesgos:
    - GET /api/risk/risks/ -> Lista todos los riesgos
    - POST /api/risk/risks/ -> Crea un nuevo riesgo
    - GET /api/risk/risks/{id}/ -> Detalle de un riesgo
    - PUT /api/risk/risks/{id}/ -> Actualiza un riesgo
    - DELETE /api/risk/risks/{id}/ -> Elimina un riesgo
    """

    queryset = Risk.objects.all().order_by("-created_at")
    serializer_class = RiskSerializer
    permission_classes = [permissions.AllowAny]  # Por ahora sin autenticación

    @action(detail=True, methods=["post"], url_path="generate-mitigations")
    def generate_mitigations(self, request, pk=None):
        """
        Genera recomendaciones de mitigación con IA para un riesgo específico
        """
        risk = self.get_object()

        recommendations = generate_mitigation_recommendations(
            risk_title=risk.title,
            risk_description=risk.description,
            likelihood=risk.likelihood,
            impact=risk.impact,
        )

        return Response(recommendations)
