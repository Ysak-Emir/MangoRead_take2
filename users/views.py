import rest_framework_simplejwt
from django.contrib.auth import authenticate
from rest_framework import generics, permissions, status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users import serializers
from users.models import User
from users.serializers import UserRegisterSerializer


class RegisterUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserRegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "Регистрация прошла успешно!",
                "data": serializer.data
            }
            return Response(data=response)
        else:
            data = serializer.errors
            return Response({"message": "Что-то пошло не так! :(",
                             "data": data})


class UserLoginAPIView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.LoginUserSerializer

    def post(self, request, format=None):
        serializer = serializers.LoginUserSerializer(data=self.request.data,
                                                     context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        password = serializer.validated_data['password']
        username = serializer.validated_data['username']
        user = authenticate(username=username, password=password)
        if user:
            refresh = rest_framework_simplejwt.tokens.RefreshToken.for_user(user)
            return Response({"refresh": str(refresh), "access": str(refresh.access_token)},
                            status=status.HTTP_202_ACCEPTED)
