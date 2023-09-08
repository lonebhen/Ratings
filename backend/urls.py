from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('accounts.urls')),
    path('rate/', include('base.urls')),
    path('api/password_reset/',
         include('django_rest_passwordreset.urls', namespace='password_reset')),


]
