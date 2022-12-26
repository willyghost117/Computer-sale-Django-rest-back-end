from django.urls import path
from django.db import router

# Django rest framework
from rest_framework.routers import DefaultRouter
#views
from .viewset.views import  ComputadoraViewSet, OrdenViewSet, OrderDetailComputerViewSet
from .viewset.component import MouseViewSet, TecladoViewSet, MonitorViewSet, ProcesadorViewSet, AltavozViewSet
#from .viewset.searchview import SearchViewSet
router = DefaultRouter()
router.register(r'mouse', MouseViewSet)
router.register(r'teclado', TecladoViewSet)
router.register(r'monitor', MonitorViewSet)
router.register(r'procesador', ProcesadorViewSet)
router.register(r'altavoz', AltavozViewSet)
router.register(r'computadora', ComputadoraViewSet)
router.register(r'orden',OrdenViewSet)
router.register(r'detalleOrden',OrderDetailComputerViewSet)
#router.register(r'search',SearchViewSet)
urlpatterns = router.urls

urlpatterns += [

]