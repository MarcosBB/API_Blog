from rest_framework import serializers
from Publicacoes import models

class PublicacoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Publicacao
        fields = 'titulo','descricao', 'autor', 'id_publicacao', 'criado'
