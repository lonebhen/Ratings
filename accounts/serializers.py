from rest_framework import serializers
from .models import PasswordResetToken


class PasswordResetTokenSerializer(serializers.Serializer):
    password = serializers.CharField(write_only = True)
    token = serializers.UUIDField(write_only = True)



class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()
    