from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.agregar, name='agregar'),
    path('dashboard/eliminar/<int:producto_id>/', views.eliminar, name='eliminar'),
]
