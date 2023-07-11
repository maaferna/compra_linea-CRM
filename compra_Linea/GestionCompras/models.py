from django.db import models

# Create your models here.
class Cliente(models.Model):
    name = models.CharField(max_length=150)
    direccion = models.TextField()
    email = models.EmailField()
    celular = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Producto(models.Model):
    name = models.CharField(max_length=150)
    categoria = models.CharField(max_length=150)
    precio = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Compra(models.Model):
    fecha = models.DateField()
    monto = models.PositiveIntegerField()

    def __str__(self):
        return self.name
