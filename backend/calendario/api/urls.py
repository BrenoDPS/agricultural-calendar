from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CulturaViewSet, 
    BandejaViewSet, 
    PlantioViewSet, 
    NotificacaoViewSet, 
    EventoViewSet
) 

# cal_router tem como função mapear os viewsets exclusivamente
cal_router = DefaultRouter()
cal_router.register(r'culturas', CulturaViewSet)
cal_router.register(r'bandejas', BandejaViewSet)
cal_router.register(r'plantios', PlantioViewSet)
cal_router.register(r'notificacoes', NotificacaoViewSet)
cal_router.register(r'eventos', EventoViewSet)

# como APIView não funciona com DefaultRouter, é necessário mapear manualmente
urlpatterns = [
    path('', include(cal_router.urls)),
]
