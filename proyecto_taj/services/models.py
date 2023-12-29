from django.contrib.auth import get_user_model
from django.db import models


# Modelo para representar las unidades de medida
class UnitOfMeasure(models.Model):
    name = models.CharField(max_length=50)


# Modelo para representar los días de la semana y sus opciones
class Schedule(models.Model):
    DAYS_OF_WEEK = [
        ('monday', 'Lunes'),
        ('tuesday', 'Martes'),
        ('wednesday', 'Miercoles'),
        ('thursday', 'Jueves'),
        ('friday', 'Viernes'),
        ('saturday', 'Sabado'),
        ('sunday', 'Domingo'),
    ]

    # Campo que almacena la selección de días
    days = models.CharField(max_length=100, choices=DAYS_OF_WEEK)
    start_time = models.TimeField()
    end_time = models.TimeField()


# Modelo para representar las categorías de servicios
class Category(models.Model):
    name = models.CharField(max_length=100)
    # Usuario que dio de alta la categoría
    staff = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='categories_created',default=None)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Modelo para representar los servicios dentro de una categoría
class Service(models.Model):
    # Categoría a la que pertenece el servicio
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='services')
    name = models.CharField(max_length=255)
    # Usuario que dio de alta el servicio
    staff = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='services_created',default=None)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Modelo para representar la relación entre un usuario, un servicio y su información asociada
class WorkerService(models.Model):
    # Usuario que ofrece el servicio
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='worker_services')
    # Servicio que se ofrece
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='workers')
    # Costo del servicio
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    # Unidad de medida para el servicio
    unit_of_measure = models.ForeignKey(UnitOfMeasure, on_delete=models.CASCADE)
    # Características del servicio
    characteristics = models.TextField()
    # Horario del servicio utilizando el modelo Schedule
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.name} - {self.service.name}"
