from rest_framework import viewsets, permissions
from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API para gestionar usuarios (listar, crear, editar, eliminar).
    """

    queryset = User.objects.all().order_by("id")
    serializer_class = UserSerializer
    permission_classes = [
        permissions.AllowAny
    ]  # luego lo cambiamos a permisos más seguros
