from rest_framework import viewsets
from .models import Security
from .serializers import SecuritySerializer


class SecurityViewSet(viewsets.ModelViewSet):
    queryset = Security.objects.all().order_by("-created_at")
    serializer_class = SecuritySerializer
