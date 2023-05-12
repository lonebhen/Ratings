from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import APIView
from .serializers import SignUpSerializer
from rest_framework.permissions import AllowAny

# Create your views here.



class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer
    permission_classes = [AllowAny]


    def post(self, request:Request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            context = {
                "message": "SignUp is Successful",
                "data": serializer.data
            }

            return Response(data=context, status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LoginView(APIView):
    permission_classes = [AllowAny,]
    def post(self, request:Request):
        username = request.data.get("username")
        password = request.data.get("password")


        user = authenticate(username=username, password=password)

        if user:
            context = {
                "message": "User successfully login",
                "tokens":user.auth_token.key
            }

            return Response(data=context, status=status.HTTP_200_OK)
        
        else:
            return Response(data={"message":"Login failed"}, status=status.HTTP_401_UNAUTHORIZED)