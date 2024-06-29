from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('contacto', views.contacto),
    path('nosotros', views.nosotros),
    path('productos', views.productos),
    path('iniciar', views.login),
    path('registrarse', views.register),
    path('carrito', views.cart),
]