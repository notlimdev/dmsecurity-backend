from rest_framework import viewsets, permissions
from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API para gestionar usuarios (listar, crear, editar, eliminar).
    """

    queryset = User.objects.all().order_by("id")
    serializer_class = UserSerializer

    # 👇 Permisos:
    # - Solo usuarios autenticados pueden listar o ver
    # - Solo administradores pueden crear, editar o eliminar
    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]
