from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUserModel(BaseUserManager):

    def create_user(self, email, password, **extra_fields):

        user = self.model(
            email=email,
            **extra_fields
        )

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff attribute as True")
        elif extra_fields.get("is_superuser") is not True:
            raise ValueError(
                "Superuser must have is_superuser attribute as True")
        elif extra_fields.get("is_active") is not True:
            raise ValueError("Superuser must have is_active attribute as True")

        return self.create_user(email=email, password=password, **extra_fields)


class User(AbstractUser):
    username = models.CharField(max_length=25, unique=True)
    email = models.EmailField(max_length=50,  unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserModel()

    def __str__(self):
        return self.email
