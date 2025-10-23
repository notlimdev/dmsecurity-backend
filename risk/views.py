from rest_framework import viewsets, permissions
from .models import Risk
from .serializers import RiskSerializer


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

