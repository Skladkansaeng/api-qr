from django.conf.urls import url
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CreateLink, LoginLink

router = DefaultRouter()
router.register('', CreateLink, 'list')
# router.register(r'test', LoginLink, 'list')
urlpatterns = [
    path('<str:token>', LoginLink.as_view({'get': 'list'}))
    ]
urlpatterns += router.urls
