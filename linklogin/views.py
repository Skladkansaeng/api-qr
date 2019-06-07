from django.contrib.auth import authenticate, login
from rest_framework import mixins, status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .serializers import UserSerializer, LoginSerializer
from .models import AuthToken


class CreateLink(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    model = AuthToken
    action_serializers = {
        'create': UserSerializer,
        'list': LoginSerializer,
    }

    def get_serializer_class(self):
        if hasattr(self, 'action_serializers'):
            if self.action in self.action_serializers:
                return self.action_serializers[self.action]
        return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({AuthToken.get_link(self.request.user, self.request.get_host())}, status=status.HTTP_201_CREATED
                        , headers=headers)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, token=AuthToken.get_token())


class LoginLink(mixins.ListModelMixin, GenericViewSet):
    serializer_class = LoginSerializer
    action_serializers = {
        'create': UserSerializer,
        'list': LoginSerializer,
    }

    def get_serializer_class(self):
        if hasattr(self, 'action_serializers'):
            if self.action in self.action_serializers:
                return self.action_serializers[self.action]
        return super().get_serializer_class()

    def list(self, request, *args, **kwargs):
        GenericViewSet.queryset = AuthToken.objects.filter(token=self.kwargs.get('token'))
        login(request, AuthToken.get_user(self.kwargs.get('token')))
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
