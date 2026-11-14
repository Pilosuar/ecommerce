from django import forms

from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'descripcion', 'categoria', 'stock', 'foto']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre del producto'}),
            'precio': forms.NumberInput(attrs={'placeholder': '0.00', 'step': '0.01', 'min': '0'}),
            'descripcion': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Detalles del producto'}),
            'categoria': forms.TextInput(attrs={'placeholder': 'Ej. Electrónica, Ropa...'}),
            'stock': forms.NumberInput(attrs={'min': '0'}),
        }
