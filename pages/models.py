from django.db import models

#Docs: https://docs.djangoproject.com/en/5.0/ref/models/fields


# Create your models here.
class Producto(models.Model):
    id_prod = models.AutoField(db_column='idProducto', primary_key=True)
    nombre = models.CharField(max_length=100, blank=False, null=False)
    stock = models.IntegerField(blank=False, null=False)
    precio = models.IntegerField(blank=False, null=False)
    descuento = models.DecimalField(blank=True, null=False, default=0, max_digits=3, decimal_places=2)

    def __str__(self):
        return str(self.nombre)

class Usuario(models.Model):
    id_user = models.AutoField(db_column='idUsuario', primary_key=True)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellido = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField()
    password = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return str(self.nombre)+" "+str(self.apellido)   

