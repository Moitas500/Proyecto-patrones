from django.db import models
from django.contrib.auth.models import User
from shop.models import Product
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class Ventas(models.Model):
    producto = models.ForeignKey(Product, related_name='ventas', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    vendedor = models.ForeignKey(User, related_name='Vendedor', on_delete=models.CASCADE)
    cliente = models.ForeignKey(User, related_name='Cliente', on_delete=models.CASCADE)
    
    class Meta:
        ordering = ('id',)
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'

    def save(self, *args, **kwargs):
        super(Ventas, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('cart:Ventas', args=[self.cliente])

    def __str__(self):
        return self.cliente.username
    
