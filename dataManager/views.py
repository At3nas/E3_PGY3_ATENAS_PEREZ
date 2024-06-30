from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto, Usuario

# Create your views here.
def dashboard(request):
    listaProductos = Producto.objects.all()
    return render(request, "dashboard.html", {"productos": listaProductos})
