#from dataclasses import field, fields
from dataclasses import field
from pyparsing import Or
from rest_framework import serializers

# models
from ..models.models import Mouse, Teclado, Monitor, Procesador, Altavoz, Computadora, Orden, OrderDetailComputer



#class MarcaSerializerComputadora(serializers.ModelField):
#    class Meta:
#        model = Marca
#        fields = '__all__'
        #depth = 2
        #print('serializador')
        #print(model)

class SerializerComputadora(serializers.ModelSerializer):
    #datosMouse = serializers.CharField(read_only = True, source = 'idMouse.marca')
    #mouse = SerializerMouse(read_only=True)
    Monitor = serializers.PrimaryKeyRelatedField(queryset=Monitor.objects.all(),source='idMonitor')
    Mouse = serializers.PrimaryKeyRelatedField(queryset=Mouse.objects.all(),source='idMouse')
    Teclado = serializers.PrimaryKeyRelatedField(queryset=Teclado.objects.all(),source='idTeclado')
    Procesador = serializers.PrimaryKeyRelatedField(queryset=Procesador.objects.all(),source='idProcesador')
    Altavoz = serializers.PrimaryKeyRelatedField(queryset=Altavoz.objects.all(),source='idAltavoz')
    

    def validate_name(self, value):
        #print(value)
        existe = Computadora.objects.filter(name__iexact=value).exists()
        #print(existe)

        if existe:
            #print('if de existe')
            raise Exception

        return value

    class Meta():
        model = Computadora
        fields = '__all__'
        depth = 1



class SerializerOrden(serializers.ModelSerializer):
    class Meta:
        model = Orden
        fields = '__all__'
        #depth =1
class SerializerOrderDetailComputer(serializers.ModelSerializer):
    #SerializerOrden(read_only=True)
    #SerializerComputadora(read_only=True)
    Computadora = serializers.PrimaryKeyRelatedField(queryset=Computadora.objects.all(),source='computadoraId')
    Orden = serializers.PrimaryKeyRelatedField(queryset=Orden.objects.all(),source='orderId')

    class Meta:
        model = OrderDetailComputer
        fields = '__all__'
        depth =2

    '''
    idMonitor = serializers.PrimaryKeyRelatedField(many = False,queryset =Monitor.objects.all())
    idMouse = serializers.PrimaryKeyRelatedField(many = False,queryset =Mouse.objects.all())
    idTeclado = serializers.PrimaryKeyRelatedField(many = False,queryset =Teclado.objects.all())
    idProcesador = serializers.PrimaryKeyRelatedField(many = False,queryset =Procesador.objects.all())
    idAltavoz = serializers.PrimaryKeyRelatedField(many = False,queryset =Altavoz.objects.all())
    '''