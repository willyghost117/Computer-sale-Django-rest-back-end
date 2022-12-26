from django.db import models
from django.db.models import F

class Component(models.Model):
    typeComponent = models.CharField(max_length=50)
    typeEntrada = models.CharField(max_length=50)

class ComponentI(Component):
    marca = models.CharField(max_length=50)
    costo = models.IntegerField()

class ComponentO(Component):
    marca = models.CharField(max_length=50)
    costo = models.IntegerField()

class Mouse(ComponentI):
    existencia = models.IntegerField()
    descripcion = models.TextField()
    fechaIngreso = models.DateTimeField(auto_now_add=True)
    fechaActualizacion = models.DateField(auto_now=True)
    def __str__(self):
        return f'Marca:{self.marca}---Dispositivo de:{self.typeComponent}---Existencia: {self.existencia}---Tipo:{self.typeEntrada}---Precio:{self.costo}'

class Teclado(ComponentI):
    existencia = models.IntegerField()
    descripcion = models.TextField()
    fechaIngreso = models.DateTimeField(auto_now_add=True)
    fechaActualizacion = models.DateField(auto_now=True)
    def __str__(self):
        return f'{self.marca}-{self.typeComponent}-{self.existencia}--{self.costo}-{self.typeEntrada}'

class Procesador(ComponentI):
    existencia = models.IntegerField()
    descripcion = models.TextField()
    fechaIngreso = models.DateTimeField(auto_now_add=True)
    fechaActualizacion = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.marca}-{self.typeComponent}-{self.existencia}--{self.costo}-{self.typeEntrada}'

class Monitor(ComponentO):
    existencia = models.IntegerField()
    descripcion = models.TextField()
    size = models.CharField(max_length=50)
    fechaIngreso = models.DateTimeField(auto_now_add=True)
    fechaActualizacion = models.DateField(auto_now=True)
    
    def __str__(self):
        return f'{self.marca}-{self.typeComponent}-{self.existencia}--{self.costo}-{self.typeEntrada}'

class Altavoz(ComponentO):
    existencia = models.IntegerField()
    descripcion = models.TextField()
    fechaIngreso = models.DateTimeField(auto_now_add=True)
    fechaActualizacion = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.marca})({self.typeComponent})({self.existencia})({self.costo})({self.typeEntrada}'

