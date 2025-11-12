# UIII_joyeria_0475/app_joyeria/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_joyeria, name='inicio_joyeria'),

    # URLs para Proveedores
    path('proveedores/agregar/', views.agregar_proveedor, name='agregar_proveedor'),
    path('proveedores/', views.ver_proveedores, name='ver_proveedores'),
    path('proveedores/actualizar/<int:id_proveedor>/', views.actualizar_proveedor, name='actualizar_proveedor'),
    path('proveedores/borrar/<int:id_proveedor>/', views.borrar_proveedor, name='borrar_proveedor'),

    # URLs para Productos
    path('productos/agregar/', views.agregar_producto, name='agregar_producto'),
    path('productos/', views.ver_productos, name='ver_productos'),
    path('productos/actualizar/<int:id_producto>/', views.actualizar_producto, name='actualizar_producto'),
    path('productos/borrar/<int:id_producto>/', views.borrar_producto, name='borrar_producto'),

    # URLs para Clientes
    path('clientes/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('clientes/', views.ver_clientes, name='ver_clientes'),
    path('clientes/actualizar/<int:id_cliente>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('clientes/borrar/<int:id_cliente>/', views.borrar_cliente, name='borrar_cliente'),

    # URLs para Empleados
    path('empleados/agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('empleados/', views.ver_empleados, name='ver_empleados'),
    path('empleados/actualizar/<int:id_empleado>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('empleados/borrar/<int:id_empleado>/', views.borrar_empleado, name='borrar_empleado'),

    # URLs para Ventas
    path('ventas/agregar/', views.agregar_venta, name='agregar_venta'),
    path('ventas/', views.ver_ventas, name='ver_ventas'),
    path('ventas/actualizar/<int:id_venta>/', views.actualizar_venta, name='actualizar_venta'),
    path('ventas/borrar/<int:id_venta>/', views.borrar_venta, name='borrar_venta'),
]