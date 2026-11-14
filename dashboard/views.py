from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProductoForm
from .models import Producto


def index(request):
    productos = Producto.objects.all()
    return render(request, 'index.html', {'productos': productos})


def agregar(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto agregado correctamente.')
            return redirect('agregar')
    else:
        form = ProductoForm()

    productos = Producto.objects.all()
    return render(request, 'agregar.html', {'form': form, 'productos': productos})


def eliminar(request, producto_id):
    if request.method == 'POST':
        producto = get_object_or_404(Producto, id=producto_id)
        producto.delete()
        messages.success(request, f'Producto "{producto.nombre}" eliminado.')
    return redirect('agregar')
