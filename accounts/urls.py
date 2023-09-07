from django.urls import path, re_path
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, PasswordResetView, PasswordResetConfirmView
from allauth.account.views import confirm_email, email_verification_sent
from django.views.generic import TemplateView


urlpatterns = [

    path('signup/', RegisterView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    re_path(r'^registration/account-confirm-email/(?P<key>.+)/$',
            confirm_email, name='account_confirm_email'),
    path("account-email-verification/", email_verification_sent,
         name="account_email_verification_sent"),

    path("user/password/reset/", PasswordResetView.as_view(),
         name="rest_password_reset"),
    path("user/password/reset/confirm/", PasswordResetConfirmView.as_view(),
         name="rest_password_reset_confirm"),

    path(
        "users/password/reset/confirm/<uidb64>/<token>/",
        TemplateView.as_view(),
        name="password_reset_confirm",
    )


]
