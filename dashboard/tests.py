import io
import os

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, TestCase
from PIL import Image

from .models import Producto


def make_png():
    buffer = io.BytesIO()
    Image.new('RGB', (20, 20), color=(37, 99, 235)).save(buffer, format='PNG')
    return buffer.getvalue()


class EcommerceSmokeTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_sin_productos(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No hay productos todavía')

    def test_dashboard_renderiza(self):
        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Agregar producto')

    def test_crear_producto_con_foto(self):
        foto = SimpleUploadedFile('foto_test.png', make_png(), content_type='image/png')
        response = self.client.post('/dashboard/', {
            'nombre': 'Producto de prueba',
            'precio': '99.90',
            'descripcion': 'Detalles de prueba',
            'categoria': 'Prueba',
            'stock': '5',
            'foto': foto,
        })
        self.assertEqual(response.status_code, 302)
        producto = Producto.objects.get()
        self.assertEqual(producto.nombre, 'Producto de prueba')
        self.assertTrue(producto.foto.url.endswith('.png'))
        self.assertTrue(os.path.exists(producto.foto.path))

        index = self.client.get('/')
        self.assertContains(index, 'Producto de prueba')
        self.assertContains(index, '99.90')

    def test_eliminar_producto(self):
        producto = Producto.objects.create(nombre='Borrar', precio='10.00')
        response = self.client.post(f'/dashboard/eliminar/{producto.id}/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Producto.objects.count(), 0)

    def test_formulario_invalido(self):
        response = self.client.post('/dashboard/', {'nombre': '', 'precio': 'abc'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['form'].errors)

    def test_css_disponibles(self):
        from django.contrib.staticfiles import finders
        for name in ('css/base.css', 'css/productos.css'):
            self.assertIsNotNone(finders.find(name), f'{name} no encontrado')
