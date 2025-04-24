from rest_framework.routers import DefaultRouter
from .views import PerfilUsuarioViewSet

router = DefaultRouter()
router.register(r'perfil', PerfilUsuarioViewSet, basename='perfil')

urlpatterns = router.urls
