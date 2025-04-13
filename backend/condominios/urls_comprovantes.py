from rest_framework.routers import DefaultRouter
from .views_comprovantes import ComprovantePagamentoViewSet

router = DefaultRouter()
router.register(r'comprovantes', ComprovantePagamentoViewSet)

urlpatterns = router.urls
