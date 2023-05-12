from django.urls import path
from .import views


urlpatterns = [

    path('',views.RatingsView.as_view(), name='ratings')
]