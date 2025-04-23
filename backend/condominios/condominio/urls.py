# condominios/condominio/urls.py

from rest_framework.routers import DefaultRouter
from condominios.condominio.views import CondominioViewSet

router = DefaultRouter()
router.register(r'', CondominioViewSet)  # endpoint base: /api/condominios/

urlpatterns = router.urls
