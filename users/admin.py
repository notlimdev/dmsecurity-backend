from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        BaseUserAdmin.fieldsets
        + (("Información adicional", {"fields": ("role", "phone", "organization")}),)
        if BaseUserAdmin.fieldsets
        else (("Información adicional", {"fields": ("role", "phone", "organization")}),)
    )

    list_display = ("username", "email", "role", "is_active", "is_staff")
    list_filter = ("role", "is_staff", "is_superuser", "is_active")
