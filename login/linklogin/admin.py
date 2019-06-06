from django.contrib import admin
from .models import AuthToken


@admin.register(AuthToken)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'token')
