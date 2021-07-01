from rest_framework import viewsets
from Autores.api import serializers
from Autores import models

class AutorViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AutoresSerializer
    queryset = models.Autor.objects.all()