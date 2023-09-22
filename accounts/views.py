from .serializers import PasswordResetRequestSerializer
from .models import PasswordResetToken
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.request import Request
from django.contrib.auth import get_user_model, authenticate
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils import timezone
import uuid
import os
from rest_framework.authtoken.models import Token

User = get_user_model()


class PasswordResetRequestView(APIView):
    permission_classes = [AllowAny]

    def post(self, request: Request):
        data = request.data

        serializer = PasswordResetRequestSerializer(data=data)

        if serializer.is_valid():
            email = serializer.validated_data['email']

            try:
                user = User.objects.get(email=email)

            except User.DoesNotExist:
                response = {
                    "message": "User with this email does not exist"
                }
                return Response(data=response, status=status.HTTP_404_NOT_FOUND)

            token = str(uuid.uuid4())
            reset_token = PasswordResetToken(user=user, token=token)
            reset_token.save()

            reset_link = f'http://localhost:4200/password/reset?token={token}'

            context = {
                'user': user,
                'reset_link': reset_link,
            }

            email_body = render_to_string(
                'account/email/user_reset_password.html', context)

            send_mail(
                'Password Reset Link',
                email_body,
                os.getenv('EMAIL_HOST_USER'),
                [email],
                fail_silently=False,
                html_message=email_body, )

            response = {
                "message": "Email reset link sent"
            }

            return Response(data=response, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetView(APIView):
    permission_classes = [AllowAny]

    def post(self, request: Request):
        data = request.data

        serializer = PasswordResetRequestSerializer(data=data)

        if serializer.is_valid():
            token = serializer.validated_data['token']
            password = serializer.validated_data['password']

            try:
                reset_token = PasswordResetToken.objects.get(
                    token=token, expires_at__gt=timezone.now())
                user = reset_token.user
                user.set_password(password)

                user.save()
                reset_token.delete()

                response = {
                    "message": "Password Reset Successfull"
                }

                return Response(data=response, status=status.HTTP_200_OK)

            except Exception as e:
                error_message = str(e)
                response = {
                    "message": f"An error occurred: {error_message}"
                }
            return Response(data=response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdminLogin(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            if user.is_active and user.is_staff:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key, 'message': 'Admin logged in successfully'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'User is not an admin'}, status=status.HTTP_403_FORBIDDEN)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
