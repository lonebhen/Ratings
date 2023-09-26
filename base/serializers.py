from .models import Ratings
# from accounts.serializers import UserSerializer
from rest_framework import serializers







class RatingSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    # user = UserSerializer()
    class Meta:
        model = Ratings
        fields = ['id','username','goals','assists','matches_played']