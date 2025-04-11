from rest_framework.routers import DefaultRouter
from .views_auditoria import AuditoriaViewSet

router = DefaultRouter()
router.register(r'auditoria', AuditoriaViewSet)

urlpatterns = router.urls
