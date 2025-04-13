from django.urls import path
from .views_relatorios import RelatorioGeralAPIView

urlpatterns = [
    path('relatorios/geral/', RelatorioGeralAPIView.as_view(), name='relatorio-geral'),
]
