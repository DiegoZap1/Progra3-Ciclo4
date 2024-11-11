from django.db import models

# Create your models here.
class usrs(models.Model):
    n_user = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.n_user
    
class publ(models.Model):
    n_user = models.ForeignKey(usrs,on_delete=models.CASCADE)
    f_pub = models.DateField()
    descrip = models.CharField(max_length=300)

class producto(models.Model):
    nombre_prod = models.CharField(max_length=100)
    precio = models.FloatField()
    f_caducidad = models.CharField(max_length=100)

class venta(models.Model):
    nombre_prod = models.ForeignKey(producto,on_delete=models.CASCADE)
    f_venta = models.DateField()
    precio_venta = models.FloatField()