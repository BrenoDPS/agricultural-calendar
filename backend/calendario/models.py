from django.db import models
from django.contrib.auth.models import User

class Cidade(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome


class Cultura(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome


class Bandeja(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome


class Plantio(models.Model):
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, 
                               null=True, blank=True)
    cultura = models.ForeignKey(Cultura, on_delete=models.CASCADE, 
                                null=True, blank=True)
    bandeja = models.ForeignKey(Bandeja, on_delete=models.CASCADE, 
                                null=True, blank=True)
    especie = models.CharField(null=True, max_length=100)
    celula = models.CharField(null=True, max_length=10)
    variedade = models.CharField(null=True, max_length=100)
    data_plantio = models.DateField()
    data_colheita = models.DateField(null=True, blank=True)
    usuario = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    dicas = models.TextField(null=True, blank=True)

    class Meta:
        unique_together = ('cidade', 'cultura', 'bandeja', 'especie', 
                           'celula', 'variedade')
    
    def __str__(self):
        return f"{self.cidade.nome} - {self.bandeja.nome}"


class Notificacao(models.Model):
    url = models.URLField(blank=True, null=True)
    titulo = models.CharField(max_length=300, null=True)
    imgUrl = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Notificação para {self.titulo}"


class Evento(models.Model):
    tipo = models.CharField(max_length=50)
    data = models.DateField()
    quantidade_mudas = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        