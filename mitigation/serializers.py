from rest_framework import serializers
from .models import MitigationPlan


class MitigationPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = MitigationPlan
        fields = "__all__"
