from .serializers import RatingSerializer
from .models import Ratings
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated




class RatingsView(APIView):
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]


    def get(self, request:Request):
        ratings = Ratings.objects.all()

        serializer = self.serializer_class(instance=ratings, many=True)

        context = {
            "message": "Ratings of the footballers",
            "data": serializer.data
        }

        return Response(data=context, status=status.HTTP_200_OK)
    

    
    
