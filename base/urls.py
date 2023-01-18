from django.urls import path
from .views import UserDetailAPI




urlpatterns = [

    path('get_details',UserDetailAPI.as_view()),
    
]