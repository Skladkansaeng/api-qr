from rest_framework.routers import DefaultRouter
from .views import CreateLink, LoginLink

router = DefaultRouter()
router.register('', CreateLink, 'list')
router.register(r'test/<str:str_id>', LoginLink, 'list')

urlpatterns = router.urls
