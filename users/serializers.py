from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializador para el modelo de usuario."""

    role_display = serializers.CharField(read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "role",
            "role_display",
            "phone",
            "organization",
            "password",
        ]
        read_only_fields = ["id", "role_display"]

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        user = User(**validated_data)
        if password:
            user.set_password(password)  # esto hashea la contraseña
        user.save()
        return user
