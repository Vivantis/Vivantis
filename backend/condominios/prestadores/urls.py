from rest_framework.routers import DefaultRouter
from .views import PrestadorViewSet  # ou .views_prestadores se for esse o nome do arquivo

router = DefaultRouter()
router.register(r'prestadores', PrestadorViewSet)

urlpatterns = router.urls
