# condominios/unidade/urls.py

from rest_framework.routers import DefaultRouter
from condominios.unidade.views import UnidadeViewSet

router = DefaultRouter()
router.register(r'', UnidadeViewSet)  # endpoint será acessado por /api/unidades/

urlpatterns = router.urls
