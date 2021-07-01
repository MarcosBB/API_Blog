from rest_framework import serializers
from Autores import models

class AutoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Autor
        fields = '__all__'
