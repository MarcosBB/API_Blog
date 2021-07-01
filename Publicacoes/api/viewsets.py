from rest_framework import viewsets
from Publicacoes.api import serializers
from Publicacoes import models

class PublicacaoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PublicacoesSerializer
    queryset = models.Publicacao.objects.all()