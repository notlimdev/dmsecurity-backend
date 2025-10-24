from rest_framework import viewsets
from .models import Incident
from .serializers import IncidentSerializer


class IncidentViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.all().order_by("-date_detected")
    serializer_class = IncidentSerializer
