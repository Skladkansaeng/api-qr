from django.db import models
from django.conf import settings
from django.utils.crypto import get_random_string


class AuthToken(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, default=None)
    token = models.CharField(max_length=50, default='')

    @staticmethod
    def get_token():
        return get_random_string(length=32)

    @staticmethod
    def get_link(user, base):
        return base + "/login/" + AuthToken.objects.get(user=user).token
