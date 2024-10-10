from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from .models import GameExpUser, Profile, Token, EmailNotification
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
    
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    

class GameExpUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = GameExpUser
        exclude = ['token']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            refresh = RefreshToken.for_user(user)

            token = Token(
                refresh_token=str(refresh),
                expired_at = timezone.now() + settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME']
            )
            token.save()

            game_exp_user = GameExpUser.objects.create(user=user, token=token, **validated_data)
            return {
                'user': GameExpUserSerializer(game_exp_user).data,
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }
        else:
            raise serializers.ValidationError(user_serializer.errors)


class GameExpUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ['user']


class EmailNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailNotification
        exclude = ['user']