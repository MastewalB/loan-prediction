from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers


class Utils:
    @staticmethod
    def encode_token(user):
        payload = {
            'id': user.id
        }
        token = RefreshToken.for_user(user)
        token.payload['TOKEN_TYPE_CLAIM'] = 'access'

        return {
            'refresh': str(token),
            'access': str(token.access_token)
        }

    @staticmethod
    def authenticate_user(validated_data):
        from .models import User
        username = validated_data['username']
        password = validated_data['password']

        user = User.objects.filter(username=username).first()
        if user and authenticate(username=username, password=password):
            return user

        raise serializers.ValidationError("Invalid Username/Password.")
