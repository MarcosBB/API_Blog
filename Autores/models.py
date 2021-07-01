from django.db import models
from uuid import uuid4

class Autor(models.Model):
    id_autor = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField('Nome',max_length=255)
    sobrenome = models.CharField('Sobrenome',max_length=255)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.nome