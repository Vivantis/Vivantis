from rest_framework.routers import DefaultRouter
from .views import RelatorioViewSet  # importa do views.py

router = DefaultRouter()
router.register(r'relatorios', RelatorioViewSet, basename='relatorios')

urlpatterns = router.urls
