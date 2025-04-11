from rest_framework.routers import DefaultRouter
from .views_autorizacoes import AutorizacaoEntradaViewSet

router = DefaultRouter()
router.register(r'autorizacoes', AutorizacaoEntradaViewSet)

urlpatterns = router.urls
