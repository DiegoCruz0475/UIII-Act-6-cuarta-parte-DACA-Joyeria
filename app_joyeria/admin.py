# UIII_joyeria_0475/app_joyeria/admin.py
from django.contrib import admin
from .models import Proveedor, Producto, Cliente, Empleado, Venta

admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(Venta)