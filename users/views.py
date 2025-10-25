from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request
from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("id")
    serializer_class = UserSerializer

    def get_permissions(self):
        """
        Define permisos por acción:
        - 'list', 'retrieve' y 'me' → autenticados
        - resto (crear, editar, eliminar) → solo admin
        """
        if self.action in ["list", "retrieve", "me"]:
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    @action(
        detail=False,
        methods=["get"],
        permission_classes=[permissions.IsAuthenticated],  # 👈 fuerza permiso explícito
        url_path="me",
    )
    def me(self, request: Request) -> Response:
        """Retorna los datos del usuario autenticado."""
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)
