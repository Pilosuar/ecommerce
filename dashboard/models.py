from django.db import models


class Producto(models.Model):
    nombre = models.CharField('nombre', max_length=200)
    precio = models.DecimalField('precio', max_digits=10, decimal_places=2)
    descripcion = models.TextField('detalles', blank=True)
    categoria = models.CharField('categoría', max_length=100, blank=True)
    stock = models.PositiveIntegerField('stock', default=0)
    foto = models.ImageField('foto', upload_to='fotos/', blank=True, null=True)
    creado_en = models.DateTimeField('creado en', auto_now_add=True)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        ordering = ['-creado_en']

    def __str__(self):
        return self.nombre
