# ─────────────────────────────────────────────────────────────
# 📅 ViewSet para Reservas de Espaços
# Permite que moradores reservem espaços e visualizem suas reservas
# ─────────────────────────────────────────────────────────────
class ReservaEspacoViewSet(viewsets.ModelViewSet):
    queryset = ReservaEspaco.objects.all().order_by('-data')
    serializer_class = ReservaEspacoSerializer
    permission_classes = get_viewset_permissions('ReservaEspacoViewSet')

    # Habilita filtros, ordenação e busca
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = [
        'morador',         # Ex: ?morador=1
        'unidade',         # Ex: ?unidade=2
        'espaco',          # Ex: ?espaco=5
        'data',            # Ex: ?data=2025-04-20
        'status'           # Ex: ?status=pendente
    ]
    ordering_fields = ['data', 'horario_inicio']   # Ex: ?ordering=data
    search_fields = ['observacoes']                # Ex: ?search=aniversario
