# UIII_joyeria_0475/app_joyeria/models.py
from django.db import models

# ==========================================
# MODELO: PROVEEDOR
# ==========================================

class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    correo = models.CharField(max_length=100)
    tipo_suministro = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# ==========================================
# MODELO: PRODUCTO
# ==========================================

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    id_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE) # Relación con Proveedor

    def __str__(self):
        return self.nombre

# ==========================================
# MODELO: CLIENTE
# ==========================================

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    correo = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre

# ==========================================
# MODELO: EMPLEADO
# ==========================================

class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    correo = models.CharField(max_length=100)
    fecha_contratacion = models.DateField()

    def __str__(self):
        return self.nombre

# ==========================================
# MODELO: VENTA
# ==========================================

class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    id_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE) # Relación con Empleado
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)   # Relación con Cliente
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE) # Relación con Producto
    fecha_venta = models.DateField()
    metodo_pago = models.CharField(max_length=50)

    def __str__(self):
        return f"Venta #{self.id_venta} - {self.id_cliente.nombre}"