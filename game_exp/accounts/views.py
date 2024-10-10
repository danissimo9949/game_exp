from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, BasePermission
from .serializers import GameExpUserSerializer, GameExpUserProfileSerializer, EmailNotificationSerializer
from .models import GameExpUser, Profile, EmailNotification

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user.user == request.user

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

class UserProfile(generics.RetrieveAPIView):
    serializer_class = GameExpUserProfileSerializer
    lookup_field = 'user__user__username'

    def get_object(self):
        profile = get_object_or_404(Profile, user__user__username=self.kwargs['username'])
        return profile

class UserProfileUpdate(generics.UpdateAPIView):
    serializer_class = GameExpUserProfileSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    
    def get_object(self):
       return get_object_or_404(Profile, user__user=self.request.user)
    
class EmailNotificationSetting(generics.RetrieveUpdateAPIView):
    serializer_class = EmailNotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
       return get_object_or_404(EmailNotification, user__user=self.request.user)
       
    
    
    