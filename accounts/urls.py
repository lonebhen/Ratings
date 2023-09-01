from django.urls import path, re_path
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView
from allauth.account.views import confirm_email, email_verification_sent


urlpatterns = [

    path('signup/', RegisterView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    re_path(r'^registration/account-confirm-email/(?P<key>.+)/$',
            confirm_email, name='account_confirm_email'),
    path("account-email-verification/", email_verification_sent,
         name="account_email_verification_sent"),
]
