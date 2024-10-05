from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import GameExpUserSerializer
from .models import GameExpUser

class UserCreate(generics.CreateAPIView):
    serializer_class = GameExpUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response_data = serializer.save()
        return Response(response_data, status=status.HTTP_201_CREATED)
    
class UserList(generics.ListAPIView):
    queryset = GameExpUser.objects.all()
    serializer_class = GameExpUserSerializer
    