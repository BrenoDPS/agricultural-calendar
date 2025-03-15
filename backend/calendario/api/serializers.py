from rest_framework import serializers
from ..models import Cultura, Bandeja, Plantio, Notificacao, Evento, Cidade

class CulturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cultura
        fields = '__all__'


class BandejaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bandeja
        fields = '__all__'


class PlantioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plantio
        fields = '__all__'


class NotificacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificacao
        fields = '__all__'


class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'


class CidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cidade
        fields = '__all__'
    