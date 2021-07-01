from django.db import models
from django.db.models.base import Model
from uuid import uuid4

class Publicacao(models.Model):
    id_publicacao = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    titulo = models.CharField('Titulo',max_length=255)
    descricao = models.TextField('Descrição', max_length=200)
    autor = models.ForeignKey('Autores.Autor', verbose_name='Autor', on_delete=models.CASCADE)
    criado = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    
    class Meta:
        verbose_name = 'Publicação'
        verbose_name_plural = 'Publicações'

    def __str__(self):
        return self.titulo