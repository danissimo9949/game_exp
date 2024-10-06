from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import GameExpUserSerializer
from .models import GameExpUser

class UserCreate(generics.CreateAPIView):
    serializer_class = GameExpUserSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response_data = serializer.save()
        return Response(response_data, status=status.HTTP_201_CREATED)
    
class UserDetail(generics.RetrieveAPIView):
    serializer_class = GameExpUserSerializer
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        user = request.user
        return Response({"message": f"Hello {request.user}"}, status=status.HTTP_200_OK)