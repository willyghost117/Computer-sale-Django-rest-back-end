from rest_framework import serializers
from ..models.models import Mouse, Teclado, Monitor, Procesador, Altavoz

class SerializerMouse(serializers.ModelSerializer):
    """"
    def validate_marca(self, value):
        print(value)
        existe = Mouse.objects.filter(marca=value).exists()
        print(existe)

        if existe:
            print('if de existe')
            raise serializers.ValidationError('Esta marca ya existe')

        return value
    """
    class Meta:
        model = Mouse
        fields = '__all__'

class SerializerTeclado(serializers.ModelSerializer):
    class Meta:
        model = Teclado
        fields = '__all__'

class SerializerMonitor(serializers.ModelSerializer):
    class Meta:
        model = Monitor
        fields = '__all__'

class SerializerProcesador(serializers.ModelSerializer):
    class Meta:
        model = Procesador
        fields = '__all__'

class SerializerAltavoz(serializers.ModelSerializer):
    class Meta:
        model = Altavoz
        fields = '__all__'