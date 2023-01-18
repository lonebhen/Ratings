from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer,RegisterSerializer
from rest_framework.authentication import TokenAuthentication

# Create your views here.


