from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Cultura, Bandeja, Plantio, Notificacao, Evento, Cidade
from .serializers import (
    CulturaSerializer, 
    BandejaSerializer, 
    PlantioSerializer, 
    NotificacaoSerializer,
    EventoSerializer,
    CidadeSerializer,
)

class CidadeViewSet(viewsets.ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer


class CulturaViewSet(viewsets.ModelViewSet):
    queryset = Cultura.objects.all()
    serializer_class = CulturaSerializer


class BandejaViewSet(viewsets.ModelViewSet):
    queryset = Bandeja.objects.all()
    serializer_class = BandejaSerializer


class PlantioViewSet(viewsets.ModelViewSet):
    queryset = Plantio.objects.all()
    serializer_class = PlantioSerializer


class NotificacaoViewSet(viewsets.ModelViewSet):
    queryset = Notificacao.objects.all()
    serializer_class = NotificacaoSerializer


class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer