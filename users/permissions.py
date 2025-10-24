from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    """Permite acceso solo a usuarios con rol ADMIN."""

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "ADMIN"


class IsAnalystOrAdmin(permissions.BasePermission):
    """Permite acceso a ANALISTA o ADMIN."""

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in [
            "ADMIN",
            "ANALISTA",
        ]
