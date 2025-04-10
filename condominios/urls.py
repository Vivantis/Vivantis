from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CondominioViewSet, UnidadeViewSet, MoradorViewSet

# O router cuida automaticamente das rotas dos ViewSets
router = DefaultRouter()
router.register(r'condominios', CondominioViewSet)
router.register(r'unidades', UnidadeViewSet)
router.register(r'moradores', MoradorViewSet)

urlpatterns = [
    path('', include(router.urls)),  # inclui todas as rotas registradas acima
]
