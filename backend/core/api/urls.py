from rest_framework.routers import DefaultRouter
from calendario.api.urls import cal_router
from django.urls import path, include

router = DefaultRouter()
# calendario
router.registry.extend(cal_router.registry)

urlpatterns = [
    path('', include(router.urls)),
]