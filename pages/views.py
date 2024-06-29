from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Página de Inicio
def home(request):
    return render(request, "index.html")

# Página de Contacto
def contacto(request):
    return render(request, "contacto.html")

# Página de Nosotros
def nosotros(request):
    return render(request, "nosotros.html")

# Página de Productos
def productos(request):
    return render(request, "productos.html")

# Página de Iniciar Sesión
def login(request):
    return render(request, "login.html")

# Página de Registrarse
def register(request):
    return render(request, "register.html")

# Página de Carrito
def cart(request):
    return render(request, "cart.html")
