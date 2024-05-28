from rest_framework.routers import DefaultRouter
from Aplicacion.api import *

router = DefaultRouter()

router.register(r"ArticuloV", ArticuloViewSet, basename="ArticuloV")

urlpatterns = router.urls