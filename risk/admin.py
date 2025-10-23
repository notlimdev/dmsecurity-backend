from django.contrib import admin
from .models import Risk


@admin.register(Risk)
class RiskAdmin(admin.ModelAdmin):
    """Configuración del admin para Risk"""

    list_display = [
        "title",
        "risk_level_name",
        "risk_level",
        "status",
        "identified_by",
        "created_at",
    ]
    list_filter = ["status", "likelihood", "impact"]
    search_fields = ["title", "description"]
    readonly_fields = ["created_at", "updated_at", "risk_level", "risk_level_name"]
