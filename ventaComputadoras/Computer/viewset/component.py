from rest_framework.views import Response
from rest_framework import viewsets

from ..models.models import Mouse, Teclado, Monitor, Procesador, Altavoz
from ..serializer.component import SerializerAltavoz, SerializerMouse, SerializerProcesador, SerializerTeclado, SerializerMonitor

class MouseViewSet(viewsets.ModelViewSet):
    queryset = Mouse.objects.all()
    serializer_class = SerializerMouse

    def get_queryset(self):
        marca = Mouse.objects.all()
        nombre = self.request.GET.get('marca')

        if nombre:
            marca = marca.filter(marca__contains=nombre)
        return marca

class TecladoViewSet(viewsets.ModelViewSet):
    queryset = Teclado.objects.all()
    serializer_class = SerializerTeclado

    def get_queryset(self):
        marca = Teclado.objects.all()
        nombre = self.request.GET.get('marca')

        if nombre:
            marca = marca.filter(marca__contains=nombre)
        return marca

class MonitorViewSet(viewsets.ModelViewSet):
    queryset = Monitor.objects.all()
    serializer_class = SerializerMonitor

    def get_queryset(self):
        marca = Monitor.objects.all()
        nombre = self.request.GET.get('marca')

        if nombre:
            marca = marca.filter(marca__contains=nombre)
        return marca

class ProcesadorViewSet(viewsets.ModelViewSet):
    queryset = Procesador.objects.all()
    serializer_class = SerializerProcesador

    def get_queryset(self):
        marca = Procesador.objects.all()
        nombre = self.request.GET.get('marca')

        if nombre:
            marca = marca.filter(marca__contains=nombre)
        return marca

class AltavozViewSet(viewsets.ModelViewSet):
    queryset = Altavoz.objects.all()
    serializer_class = SerializerAltavoz

    def get_queryset(self):
        marca = Altavoz.objects.all()
        nombre = self.request.GET.get('marca')

        if nombre:
            marca = marca.filter(marca__contains=nombre)
        return marca