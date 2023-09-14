from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('accounts.urls')),
    path('rate/', include('base.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls'))


]
