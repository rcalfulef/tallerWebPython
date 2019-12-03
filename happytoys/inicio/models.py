from django.db import models

# Create your models here.

class Juguete(models.Model):
    nombre = models.CharField(max_length = 100,blank = False, null = False,verbose_name = "Nombre juguete")
    precio = models.IntegerField(blank = True,null = True,verbose_name = "Precio juguete")
    cantidad = models.IntegerField(blank = True,null = True,verbose_name = "Cantidad juguete")
    descripcion =  models.CharField(max_length = 500,blank = False, null =  False,verbose_name = "Descripcion")
    def __str__(self):
        return u'%s' %(self.nombre)
    

class Boleta(models.Model):
    fecha = models.DateTimeField(blank = False, null = False, auto_now_add = True,verbose_name = "Fecha boleta")
    total = models.IntegerField(blank = False, null = False,verbose_name = "Total boleta")
    juguete = models.ForeignKey(Juguete,on_delete=models.CASCADE,blank = False,null = True)
    def __str__(self):
        return u'%s' %(self.fecha)

class Image(models.Model):
    name = models.CharField(max_length=500)
    imageFile = models.FileField(upload_to='images/', null = True, verbose_name= "")
    
    def __str__(self):
        return self.name + ": " + str(self.imageFile)