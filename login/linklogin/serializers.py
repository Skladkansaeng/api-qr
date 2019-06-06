from django.contrib.auth.models import User
from rest_framework import serializers
from .models import AuthToken


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthToken
        fields = ()


class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
        )


class LoginSerializer(serializers.ModelSerializer):
    user = GetUserSerializer

    class Meta:
        model = AuthToken
        fields = ('user'
                  )
