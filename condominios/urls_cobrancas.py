from rest_framework.routers import DefaultRouter
from .views_cobrancas import CobrancaViewSet

router = DefaultRouter()
router.register(r'cobrancas', CobrancaViewSet)

urlpatterns = router.urls
