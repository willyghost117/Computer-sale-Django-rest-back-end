
#from unittest import expectedFailure
#from urllib import response
from rest_framework import status
from django import views
from requests import request
#from django.forms import ValidationError
#from django.shortcuts import render

"""Django rest framework"""

from rest_framework.views import Response
from rest_framework import viewsets

#from rest_framework import status


# Create your views here.

from ..models.models import Computadora, Orden, OrderDetailComputer
from ..serializer.serializers import  SerializerComputadora, SerializerOrden, SerializerOrderDetailComputer




class ComputadoraViewSet(viewsets.ModelViewSet):
    #print('view')
    #print(viewsets.ModelViewSet)
    queryset = Computadora.objects.all()
    #print(queryset)
    serializer_class = SerializerComputadora
    #print(serializer_class)

    
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data = request.data)
        try: 
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'Pc agregada'},status = status.HTTP_201_CREATED)
        except Exception:
            return Response({'message':'No se creo la pc, el stock es insuficiente o la computadora ya existe'},status=status.HTTP_400_BAD_REQUEST)


    def get_queryset(self):
        computadora = Computadora.objects.all()
        nombre = self.request.GET.get('name')

        if nombre:
            computadora = computadora.filter(name__contains=nombre)
        return computadora
        
    

class OrdenViewSet(viewsets.ModelViewSet):
    queryset = Orden.objects.all()
    serializer_class = SerializerOrden



class OrderDetailComputerViewSet(viewsets.ModelViewSet):
    queryset = OrderDetailComputer.objects.all()
    serializer_class = SerializerOrderDetailComputer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data = request.data)
        try: 
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'Pc agregada a la orden'},status = status.HTTP_201_CREATED)
        except Exception:
            return Response({'message':'Pc no agregada a la orden, revisa el stock'},status=status.HTTP_400_BAD_REQUEST)
    """"
    def create(self, request, *args, **kwargs):
        pc = super().create(request, *args, **kwargs)
        if pc.data['id'] is not None:
            return pc   
        else:
            return Response({'message': 'Falta stock'})

    
    def create(self, request, *args, **kwargs):
        try:
            super().create(self, request, *args, **kwargs)
            return Response({'message':'Computadora creada'})
        except Exception as ve:
            return Response({'message':ve,"stock':False})

    
    """        
    #def crete(self, request, *args, **kwargs):
    #    pc = super().create(request, *args, **kwargs)
    #    if pc is 201:
    #        return pc
    #    else:
    #        return views.Response({"message":"No hay stock"})
    
    #def create(self, request):
        #Llamamos el metodo create del ApiView y es por es donde se crea el objeto
     #   result = super(ComputadoraViewSet, self).create(request)
     #   return result({'success': True, 'message': 'Creado correctamente'})



#class ComponenteViewSet(viewsets.ModelViewSet):
#    queryset = ComponenteViewSet.objects.all()


    

