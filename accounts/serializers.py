from dj_rest_auth.serializers import PasswordResetSerializer


class CustomPasswordResetSerializer(PasswordResetSerializer):
    def get_email_options(self):
        return {
            "email_template_name": "account/email/user_reset_password.html"
        }
    

