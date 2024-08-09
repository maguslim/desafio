from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from decimal import Decimal


class Campo(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    cidade = models.CharField(max_length=100, default='')
    endereco = models.CharField(max_length=255)
    descricao = models.TextField()
    preco_hora = models.DecimalField(max_digits=10, decimal_places=2)
    locador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='campos')

    tipo_gramado = models.CharField(max_length=50, choices=[
        ('natural', 'Natural'),
        ('sintetico', 'Sintético'),
    ], null=True)

    iluminacao = models.BooleanField(default=False)
    vestiarios = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

class CampoFoto(models.Model):
    campo = models.ForeignKey(Campo, on_delete=models.CASCADE, related_name='fotos')
    imagem = models.ImageField(upload_to='campo_pictures/')

    def __str__(self):
        return f"Foto de {self.campo.nome}"

class Reserva(models.Model):
    campo = models.ForeignKey(Campo, on_delete=models.CASCADE, related_name='reservas')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservas')
    data_reserva = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    criado_em = models.DateTimeField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        unique_together = ('campo', 'data_reserva', 'hora_inicio')

    def __str__(self):
        return f"Reserva de {self.campo.nome} por {self.usuario.username} em {self.data_reserva}"


    def calcular_valor_total(self):
        hora_inicio = datetime.strptime(self.hora_inicio, '%H:%M').time()
        hora_fim = datetime.strptime(self.hora_fim, '%H:%M').time()

        hoje = datetime.today().date()
        inicio = datetime.combine(hoje, hora_inicio)
        fim = datetime.combine(hoje, hora_fim)

        duracao = fim - inicio
        duracao_horas = duracao.total_seconds() / 3600

        preco_hora_decimal = Decimal(self.campo.preco_hora)
        valor_total = preco_hora_decimal * Decimal(duracao_horas)
        return valor_total