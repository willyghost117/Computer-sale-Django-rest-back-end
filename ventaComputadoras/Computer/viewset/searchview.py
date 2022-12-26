"""Models and serializers"""
from ..models.component import Mouse, Monitor, Procesador, Teclado, Altavoz
from ..serializer.component import SerializerMouse, SerializerAltavoz

"""Rest """
from rest_framework.views import Response
from rest_framework import viewsets
from ..viewset.component import MouseViewSet, MonitorViewSet, TecladoViewSet, ProcesadorViewSet, AltavozViewSet
from django.utils  import timezone
"""Class for search 
class SearchViewSet(viewsets.ModelViewSet):
    #nombre = self.request.GET.get('name')
    #queryset = MouseViewSet,MonitorViewSet,TecladoViewSet, ProcesadorViewSet, AltavozViewSet
    #queryset = Mouse.objects.all()
    #queryset = Altavoz.objects.all()
    #serializer_class = SerializerMouse
    #serializer_class = SerializerAltavoz
 
class ComponenteDayView(viewsets.ModelViewSet):
    queryset = Componente.objects.all()
    serializer_class = ComponenteMarcaSerializer

    def obtenerDatosComponentes(self, yesterday, today):
      ratonC = Mouse.objects.filter(fechaIngreso__range=(yesterday, today))
      tecladoC = Teclado.objects.filter(fechaIngreso__range=(yesterday, today))
      monitorC =  Monitor.objects.filter(fechaIngreso__range=(yesterday, today))
      altavozC =  Altavoz.objects.filter(fechaIngreso__range=(yesterday, today))
      procesadorC = Procesador.objects.filter(fechaIngreso__range=(yesterday, today)) 

      if ratonC or tecladoC or monitorC or altavozC or procesadorC:
        finalData = chain(ratonC, tecladoC, monitorC, altavozC, procesadorC, placaC)
        serializer = ComponenteMarcaSerializer(finalData, many=True)
        return views.Response({'status': True, 'message': 'Componentes encontrados',
        'data': serializer.data}, status=status.HTTP_200_OK)
      else:
        return views.Response({'status': False, 'message': 'No hay componentes creados hace un dia',}
        , status=status.HTTP_204_NO_CONTENT)


    def list(self, request, *args, **kwargs):
      try:
        yesterday = timezone.now() - timezone.timedelta(days=1)
        today = timezone.now() #  - datetime.timedelta(days=2)
        tipo = request.query_params.get('tipo')
        if tipo == 'componente':
          return self.obtenerDatosComponentes(yesterday, today)
        else:
          return views.Response({'message': 'No envio ninguna query valida',
          'status': False}, status=status.HTTP_404_NOT_FOUND)
      except Exception as e:
        return views.Response({'message': 'Error',
        'status': str(e)}, status=status.HTTP_400_BAD_REQUEST)
"""