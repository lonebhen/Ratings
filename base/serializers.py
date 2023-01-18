from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from base.models import Ratings



class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        field = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = ["id","first_name","last_name","username"]


"""Registration Serializer"""
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required = True, validators = [UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(required = True,validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(required = True, write_only = True, validators=[validate_password])
    password2 = serializers.CharField(write_only = True, required = True)

    class Meta:
        model = User
        field = ('username','password','password2','email','first_name','last_name',)
        extra_kwargs = {
            'first_name':{'required':True},
            'last_name':{'required':True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password":"Password fields don't match"})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'],email=validated_data['email'],first_name=validated_data['first_name'],
        last_name=validated_data['last_name'])
        user.set_password(validated_data['password'])
        user.save()
        return user








