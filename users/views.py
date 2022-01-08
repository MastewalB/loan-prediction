from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from users.serializers import LoginSerializer, UserSerializer
from users.utils import Utils
from users.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
# Create your views here.


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data

        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user = User.objects.get(email=email)
        token = Utils.encode_token(user)

        return Response({
            "data": serializer.data,
            "token": token
        })


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = Utils.authenticate_user(serializer.validated_data)
        validated_user = UserSerializer(user)
        token = Utils.encode_token(user)

        return Response({
            "data": validated_user.data,
            "token": token
        })
