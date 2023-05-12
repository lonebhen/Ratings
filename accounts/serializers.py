from .models import User
from rest_framework import serializers
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token





class SignUpSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=25)
    email = serializers.CharField(max_length = 45)
    password = serializers.CharField(min_length = 8, write_only=True)


    class Meta:
        model = User
        fields = ['username','email','password']



    def validate(self, attrs):
        username_exits = User.objects.filter(username=attrs["username"]).exists()

        if username_exits:
            raise ValidationError("Username already exists")
        return super().validate(attrs)
    


    def create(self, validated_data):
        password = validated_data.pop("password")

        user = super().create(validated_data)

        user.set_password(password)
        user.save()

        Token.objects.create(user=user)

        return user
    


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username']