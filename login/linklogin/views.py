from django.http import JsonResponse
from rest_framework import mixins, status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .serializers import UserSerializer, LoginSerializer
from .models import AuthToken


class CreateLink(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    model = AuthToken

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({AuthToken.get_link(self.request.user, self.request.get_host())}, status=status.HTTP_201_CREATED
                        , headers=headers)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, token=AuthToken.get_token())


# def LoginLink(request, str_id):
#     print(request.user)
#     return JsonResponse({}, status=status.HTTP_200_OK)
class LoginLink(mixins.ListModelMixin, GenericViewSet):
    serializer_class = LoginSerializer

    def list(self, request, *args, **kwargs):
        query = AuthToken.objects.filter(self.request.user)
        return Response(LoginSerializer(query).data)
