from django.contrib.auth.models import User
from .models import GameExpUser
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
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            game_exp_user = GameExpUser.objects.create(user=user, **validated_data)
            refresh = RefreshToken.for_user(user)
            return {
                'user': GameExpUserSerializer(game_exp_user).data,
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }
        else:
            raise serializers.ValidationError(user_serializer.errors)

        