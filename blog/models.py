from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):

    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField('Título', max_length=200)
    conteudo = models.TextField('Conteúdo')
    imagem = models.ImageField(upload_to='imagens/')

    data_criacao = models.DateTimeField('Data de criação', auto_now=True)
    data_atualizacao = models.DateTimeField('Data de atualizacao', auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.titulo, self.autor)
