from rest_framework.routers import DefaultRouter
from .views import MoradorViewSet  # Import do novo módulo moradores

router = DefaultRouter()
router.register(r'moradores', MoradorViewSet)

urlpatterns = router.urls
