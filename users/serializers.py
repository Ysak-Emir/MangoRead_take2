from .models import User
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework import serializers


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    password2 = serializers.CharField(max_length=128, min_length=8, write_only=True)


    class Meta:
        model = User
        fields = ["username", "nickname", "password", "password2"]

    def save(self, *args, **kwargs):
        user = User(
            username=self.validated_data["username"],
            nickname=self.validated_data["nickname"],
        )
        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]
        if password != password2:
            raise serializers.ValidationError({password: "Пароли не совпадают!"})
        user.set_password(password)
        user.save()
        return user


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField(
        label="Username",
        write_only=True
    )
    password = serializers.CharField(
        label="Password",
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                msg = 'Доступ запрещен: неправильное имя пользователя или пароль.'
                raise serializers.ValidationError({"password": msg}, code='authorization')
        else:
            msg = 'Требуются как «имя пользователя», так и «пароль».'
            raise serializers.ValidationError(msg, code='authorization')
        attrs['user'] = user
        return attrs