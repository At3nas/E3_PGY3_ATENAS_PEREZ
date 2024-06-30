from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard),
    path('edicionProducto/<id>', views.edicionProducto),
    path('agregarProducto/', views.agregarProducto),
    path('eliminarProducto/<id>', views.eliminarProducto),
]