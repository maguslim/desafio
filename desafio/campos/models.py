from django.db import models
from django.contrib.auth.models import User

class Campo(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    descricao = models.TextField()
    preco_hora = models.DecimalField(max_digits=10, decimal_places=2)
    locador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='campos')

    def __str__(self):
        return self.nome

class CampoFoto(models.Model):
    campo = models.ForeignKey(Campo, on_delete=models.CASCADE, related_name='fotos')
    imagem = models.ImageField(upload_to='campo_pictures/')

    def __str__(self):
        return f"Foto de {self.campo.nome}"
