#from logging import exception
#from pyexpat import model
#from tkinter import CASCADE
from ast import Raise

from django.db import models
from django.db.models import F
from .component import Monitor, Mouse, Teclado, Procesador, Altavoz
# Create your models here.
#class Dispositivo(models.Model):
    
#    marca = models.CharField(max_length=50)

    #def __str__(self):
    #    return f'{self.marca}'



    #def __str__(self):
    #    return f'{self.marca}'



class Computadora(models.Model):
    name = models.CharField(max_length=50)
    idMonitor = models.ForeignKey(Monitor, on_delete=models.CASCADE)
    idMouse = models.ForeignKey(Mouse, on_delete=models.CASCADE)
    idTeclado = models.ForeignKey(Teclado, on_delete=models.CASCADE)
    idProcesador = models.ForeignKey(Procesador,on_delete=models.CASCADE)
    idAltavoz = models.ForeignKey(Altavoz,on_delete=models.CASCADE)
    existencia = models.IntegerField()
    total = models.IntegerField(null=True)
    
    def decrementar_cantidad(self):
        monitor = Monitor.objects.filter(id=self.idMonitor.id)
        mouse = Mouse.objects.filter(id=self.idMouse.id)
        teclado = Teclado.objects.filter(id=self.idTeclado.id)
        procesador = Procesador.objects.filter(id=self.idProcesador.id)
        altavoz = Altavoz.objects.filter(id=self.idAltavoz.id)
        print('ejecutando')

        if (monitor[0].existencia>= self.existencia and
            mouse[0].existencia>= self.existencia and
            teclado[0].existencia >= self.existencia and
            procesador[0].existencia >= self.existencia and
            altavoz[0].existencia >= self.existencia 
            ):
            monitor.update(existencia=F('existencia')-self.existencia)
            mouse.update(existencia=F('existencia')-self.existencia)
            teclado.update(existencia=F('existencia')-self.existencia)
            procesador.update(existencia=F('existencia')-self.existencia)
            altavoz.update(existencia=F('existencia')-self.existencia)
            total = monitor[0].costo + mouse[0].costo + teclado[0].costo + teclado[0].costo + procesador[0].costo + altavoz[0].costo
            print(total)
            return total
        else:
            return Exception
        
    
    
    def save(self, *args, **kwargs): 
        """Drecremento"""
        resultado = self.decrementar_cantidad()
        #print(resultado)
        if not False:
            #print('ingresando el if')
            self.total= resultado
            #print('guardando desde save')
            super(Computadora,self).save(*args, **kwargs)
            
        else:
            return Exception
       
    
    def __str__(self):
        #print('model')
        #print(self.name)
        return f'{self.name}---Total: {self.total}--Existencia :{self.existencia}'

class Orden(models.Model):
    numOrden = models.IntegerField()
    total =models.IntegerField(null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f'{self.numOrden}'

class OrderDetailComputer(models.Model):
    computadoraId = models.ForeignKey(Computadora,on_delete=models.CASCADE)
    orderId = models.ForeignKey(Orden,on_delete=models.CASCADE)

    existencia = models.IntegerField(blank=True, null=True)
    totalOrder = models.IntegerField(null=True,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    

    def decrementar_cantidad(self):
        computadora = Computadora.objects.filter(id=self.computadoraId.id)

        print('ejecutando')

        if (computadora[0].existencia>= self.existencia  
            ):
            computadora.update(existencia=F('existencia')-self.existencia)
            total = computadora[0].total* self.existencia
            print(total)
            return total
        else:
            return Exception
        
    
    
    def save(self, *args, **kwargs): 
        """Drecremento"""
        resultado = self.decrementar_cantidad()
        """
        ordenD = OrderDetailComputer.objects.filter(id=self.orderId.id)
        total = ordenD[0].totalOrder + self.totalOrder
        self.total = total
        super(Orden, self).save(*args, **kwargs)
        #print(resultado)
        """
        if not False:
            #print('ingresando el if')
            self.totalOrder= resultado
            #print('guardando desde save')
            super(OrderDetailComputer, self).save(*args, **kwargs)

            
        else:
            return Exception


    def __str__(self):
        return f'Orden :{self.orderId} Pc para la orden :{self.computadoraId}'











"""
    def decrementar_cantidad(self):
        computadora = Computadora.objects.filter(id=self.computadoraId.id)
        print('ejecutando')

        if (computadora[0].existencia>= self.existencia 
            ):
            computadora.update(existencia=F('existencia')-self.existencia)
            total = computadora[0].costo + computadora[0].costo
            print(total)
            return total
        else:
            return Exception
        
    
    
    def save(self, *args, **kwargs): 
        Drecremento
        resultado = self.decrementar_cantidad()
        print(resultado)
        if not False:
            print('ingresando el if')
            self.total= resultado
            print('guardando desde save')
            super(Orden,self).save(*args, **kwargs)
    
    
    


#Monitor.objects.filter(id=self.idMonitor.id).update(existencia=F('existencia')-1)
       if ((Mouse.objects.get(id=self.idMouse.id).existencia ==0)):
            return self.idMonitor.marca
       
       elif ((Teclado.objects.get(id=self.idTeclado.id).existencia ==0)):
            return self.idMonitor.marca

       elif ((Monitor.objects.get(id=self.idMonitor.id).existencia ==0)):
            return self.idMonitor.marca

       else:     
            Mouse.objects.filter(id=self.idMouse.id).update(existencia=F('existencia')-1)
            Teclado.objects.filter(id=self.idTeclado.id).update(existencia=F('existencia')-1)
       #Monitor.objects.filter(pk=Computadora).update(F('acumulador')+1)
            Monitor.objects.filter(id=self.idMonitor.id).update(existencia=F('existencia')-1)
            super(Computadora,self).save(*args, **kwargs)
"""
