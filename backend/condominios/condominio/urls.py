# condominios/condominio/urls.py
from rest_framework.routers import DefaultRouter
from .views import CondominioViewSet, UnidadeViewSet

router = DefaultRouter()
router.register(r'condominios', CondominioViewSet)
router.register(r'unidades', UnidadeViewSet)

urlpatterns = router.urls
