from django.db import models

class Usuario(models.Model):
    cedula = models.BigIntegerField(unique=True, primary_key=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    celular = models.BigIntegerField()
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_ingreso = models.DateField()
    cargo = models.CharField(max_length=100)
    eps = models.CharField(max_length=100)
    pension = models.CharField(max_length=100)

    objects = models.Manager()

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"


class Desprendible(models.Model):
    usuario_cedula = models.BigIntegerField(default=0)
    horas_extra_diurna = models.IntegerField(default=0)
    horas_extra_nocturna = models.IntegerField(default=0)
    horas_extra_diurna_dominical = models.IntegerField(default=0)
    horas_extra_nocturna_dominical = models.IntegerField(default=0)
    total_hed = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_hen = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_hedd = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_hend = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_horas_extras = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    auxilio_transporte = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    descuento_salud = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    descuento_pension = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    objects = models.Manager()

    def __str__(self):
        return f"Desprendible de usuario con cédula {self.usuario_cedula}"
