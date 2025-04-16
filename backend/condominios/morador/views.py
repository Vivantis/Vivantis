# ─────────────────────────────────────────────────────────────
# 👤 ViewSet para o modelo Morador
# ─────────────────────────────────────────────────────────────
class MoradorViewSet(viewsets.ModelViewSet):
    queryset = Morador.objects.all()
    serializer_class = MoradorSerializer
    permission_classes = get_viewset_permissions('MoradorViewSet')
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['email', 'unidade']
    search_fields = ['nome']

    # ✅ POST /api/moradores/{id}/aprovar/
    @action(detail=True, methods=['post'], url_path='aprovar')
    def aprovar_morador(self, request, pk=None):
        morador = self.get_object()
        if morador.user:
            morador.user.is_active = True
            morador.user.save()
            return Response({'status': 'Morador aprovado com sucesso'}, status=status.HTTP_200_OK)
        return Response({'error': 'Morador não possui usuário vinculado'}, status=status.HTTP_400_BAD_REQUEST)

    # ✅ PATCH /api/moradores/{id}/delegar-voto/
    @action(detail=True, methods=['patch'], url_path='delegar-voto')
    def delegar_voto(self, request, pk=None):
        """
        Permite que um admin/síndico altere o campo pode_votar de um morador.
        Body esperado: { "pode_votar": true/false }
        """
        morador = self.get_object()
        if 'pode_votar' not in request.data:
            return Response({'error': 'Campo "pode_votar" é obrigatório.'}, status=status.HTTP_400_BAD_REQUEST)

        pode_votar = request.data.get('pode_votar')

        if pode_votar is None:
           return Response({'error': 'Campo "pode_votar" é obrigatório.'}, status=status.HTTP_400_BAD_REQUEST)


        morador.pode_votar = pode_votar
        morador.save()
        return Response({
            'status': 'Atualização de voto realizada com sucesso',
            'morador': morador.nome,
            'pode_votar': morador.pode_votar
        }, status=status.HTTP_200_OK)
