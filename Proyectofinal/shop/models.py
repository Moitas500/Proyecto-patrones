from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    nombre = models.CharField(max_length=200, db_index=True)
    descripcion = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('nombre',)
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def save(self, *args, **kwargs):
        if not self.descripcion:
            self.descripcion = slugify(self.nombre)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.descripcion])

    def __str__(self):
        return self.nombre


class Product(models.Model):
    categoria = models.ForeignKey(
        Category, related_name='productos', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200, db_index=True)
    descripcion = models.SlugField(max_length=200, db_index=True)
    imagen = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    existencia = models.PositiveIntegerField()
    disponible = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('nombre',)
        index_together = (('id', 'descripcion'),)
        verbose_name = 'producto'
        verbose_name_plural = 'Productos'

    def save(self, *args, **kwargs):
        if not self.descripcion:
            self.descripcion = slugify(self.nombre)
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.descripcion])

    def __str__(self):
        return self.nombre
