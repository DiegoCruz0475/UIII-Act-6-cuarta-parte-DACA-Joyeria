# UIII_joyeria_0475/app_joyeria/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Proveedor, Producto, Cliente, Empleado, Venta

def inicio_joyeria(request):
    return render(request, 'inicio.html')

# ==========================================
# VISTAS PARA PROVEEDOR
# ==========================================
def agregar_proveedor(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        tipo_suministro = request.POST.get('tipo_suministro')

        proveedor = Proveedor(
            nombre=nombre,
            direccion=direccion,
            telefono=telefono,
            correo=correo,
            tipo_suministro=tipo_suministro
        )
        proveedor.save()
        return redirect('ver_proveedores')
    return render(request, 'proveedor/agregar_proveedor.html')

def ver_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedor/ver_proveedores.html', {'proveedores': proveedores})

def actualizar_proveedor(request, id_proveedor):
    proveedor = get_object_or_404(Proveedor, pk=id_proveedor)
    if request.method == 'POST':
        proveedor.nombre = request.POST.get('nombre')
        proveedor.direccion = request.POST.get('direccion')
        proveedor.telefono = request.POST.get('telefono')
        proveedor.correo = request.POST.get('correo')
        proveedor.tipo_suministro = request.POST.get('tipo_suministro')
        proveedor.save()
        return redirect('ver_proveedores')
    return render(request, 'proveedor/actualizar_proveedor.html', {'proveedor': proveedor})

def borrar_proveedor(request, id_proveedor):
    proveedor = get_object_or_404(Proveedor, pk=id_proveedor)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('ver_proveedores')
    return render(request, 'proveedor/borrar_proveedor.html', {'proveedor': proveedor})

# ==========================================
# VISTAS PARA PRODUCTO
# ==========================================
def agregar_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        tipo = request.POST.get('tipo')
        material = request.POST.get('material')
        precio = request.POST.get('precio')
        id_proveedor = request.POST.get('id_proveedor')

        proveedor = get_object_or_404(Proveedor, pk=id_proveedor)

        producto = Producto(
            nombre=nombre,
            tipo=tipo,
            material=material,
            precio=precio,
            id_proveedor=proveedor
        )
        producto.save()
        return redirect('ver_productos')
    proveedores = Proveedor.objects.all()
    return render(request, 'producto/agregar_producto.html', {'proveedores': proveedores})

def ver_productos(request):
    productos = Producto.objects.all()
    return render(request, 'producto/ver_productos.html', {'productos': productos})

def actualizar_producto(request, id_producto):
    producto = get_object_or_404(Producto, pk=id_producto)
    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.tipo = request.POST.get('tipo')
        producto.material = request.POST.get('material')
        producto.precio = request.POST.get('precio')
        id_proveedor = request.POST.get('id_proveedor')
        producto.id_proveedor = get_object_or_404(Proveedor, pk=id_proveedor)
        producto.save()
        return redirect('ver_productos')
    proveedores = Proveedor.objects.all()
    return render(request, 'producto/actualizar_producto.html', {'producto': producto, 'proveedores': proveedores})

def borrar_producto(request, id_producto):
    producto = get_object_or_404(Producto, pk=id_producto)
    if request.method == 'POST':
        producto.delete()
        return redirect('ver_productos')
    return render(request, 'producto/borrar_producto.html', {'producto': producto})


# ==========================================
# VISTAS PARA CLIENTE
# ==========================================
def agregar_cliente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')

        cliente = Cliente(
            nombre=nombre,
            direccion=direccion,
            telefono=telefono,
            correo=correo,
            fecha_nacimiento=fecha_nacimiento
        )
        cliente.save()
        return redirect('ver_clientes')
    return render(request, 'cliente/agregar_cliente.html')

def ver_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/ver_clientes.html', {'clientes': clientes})

def actualizar_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, pk=id_cliente)
    if request.method == 'POST':
        cliente.nombre = request.POST.get('nombre')
        cliente.direccion = request.POST.get('direccion')
        cliente.telefono = request.POST.get('telefono')
        cliente.correo = request.POST.get('correo')
        cliente.fecha_nacimiento = request.POST.get('fecha_nacimiento')
        cliente.save()
        return redirect('ver_clientes')
    return render(request, 'cliente/actualizar_cliente.html', {'cliente': cliente})

def borrar_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, pk=id_cliente)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_clientes')
    return render(request, 'cliente/borrar_cliente.html', {'cliente': cliente})

# ==========================================
# VISTAS PARA EMPLEADO
# ==========================================
def agregar_empleado(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        puesto = request.POST.get('puesto')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        fecha_contratacion = request.POST.get('fecha_contratacion')

        empleado = Empleado(
            nombre=nombre,
            puesto=puesto,
            telefono=telefono,
            correo=correo,
            fecha_contratacion=fecha_contratacion
        )
        empleado.save()
        return redirect('ver_empleados')
    return render(request, 'empleado/agregar_empleado.html')

def ver_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleado/ver_empleados.html', {'empleados': empleados})

def actualizar_empleado(request, id_empleado):
    empleado = get_object_or_404(Empleado, pk=id_empleado)
    if request.method == 'POST':
        empleado.nombre = request.POST.get('nombre')
        empleado.puesto = request.POST.get('puesto')
        empleado.telefono = request.POST.get('telefono')
        empleado.correo = request.POST.get('correo')
        empleado.fecha_contratacion = request.POST.get('fecha_contratacion')
        empleado.save()
        return redirect('ver_empleados')
    return render(request, 'empleado/actualizar_empleado.html', {'empleado': empleado})

def borrar_empleado(request, id_empleado):
    empleado = get_object_or_404(Empleado, pk=id_empleado)
    if request.method == 'POST':
        empleado.delete()
        return redirect('ver_empleados')
    return render(request, 'empleado/borrar_empleado.html', {'empleado': empleado})

# ==========================================
# VISTAS PARA VENTA
# ==========================================
def agregar_venta(request):
    if request.method == 'POST':
        id_empleado = request.POST.get('id_empleado')
        id_cliente = request.POST.get('id_cliente')
        id_producto = request.POST.get('id_producto')
        fecha_venta = request.POST.get('fecha_venta')
        metodo_pago = request.POST.get('metodo_pago')

        empleado = get_object_or_404(Empleado, pk=id_empleado)
        cliente = get_object_or_404(Cliente, pk=id_cliente)
        producto = get_object_or_404(Producto, pk=id_producto)

        venta = Venta(
            id_empleado=empleado,
            id_cliente=cliente,
            id_producto=producto,
            fecha_venta=fecha_venta,
            metodo_pago=metodo_pago
        )
        venta.save()
        return redirect('ver_ventas')
    empleados = Empleado.objects.all()
    clientes = Cliente.objects.all()
    productos = Producto.objects.all()
    return render(request, 'venta/agregar_venta.html', {
        'empleados': empleados,
        'clientes': clientes,
        'productos': productos
    })

def ver_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'venta/ver_ventas.html', {'ventas': ventas})

def actualizar_venta(request, id_venta):
    venta = get_object_or_404(Venta, pk=id_venta)
    if request.method == 'POST':
        venta.id_empleado = get_object_or_404(Empleado, pk=request.POST.get('id_empleado'))
        venta.id_cliente = get_object_or_404(Cliente, pk=request.POST.get('id_cliente'))
        venta.id_producto = get_object_or_404(Producto, pk=request.POST.get('id_producto'))
        venta.fecha_venta = request.POST.get('fecha_venta')
        venta.metodo_pago = request.POST.get('metodo_pago')
        venta.save()
        return redirect('ver_ventas')
    empleados = Empleado.objects.all()
    clientes = Cliente.objects.all()
    productos = Producto.objects.all()
    return render(request, 'venta/actualizar_venta.html', {
        'venta': venta,
        'empleados': empleados,
        'clientes': clientes,
        'productos': productos
    })

def borrar_venta(request, id_venta):
    venta = get_object_or_404(Venta, pk=id_venta)
    if request.method == 'POST':
        venta.delete()
        return redirect('ver_ventas')
    return render(request, 'venta/borrar_venta.html', {'venta': venta})