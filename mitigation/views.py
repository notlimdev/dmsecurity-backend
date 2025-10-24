from rest_framework import viewsets
from .models import MitigationPlan
from .serializers import MitigationPlanSerializer


class MitigationPlanViewSet(viewsets.ModelViewSet):
    queryset = MitigationPlan.objects.all().order_by("-created_at")
    serializer_class = MitigationPlanSerializer
