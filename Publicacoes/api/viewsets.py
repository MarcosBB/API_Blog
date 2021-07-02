from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from Publicacoes.api import serializers
from Publicacoes import models

class PublicacaoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PublicacoesSerializer
    queryset = models.Publicacao.objects.all()
    filter_backends = [SearchFilter]
    search_fields =['autor__nome', 'autor__id_autor', 'autor__sobrenome']


