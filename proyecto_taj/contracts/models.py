from django.db import models
from django.contrib.auth import get_user_model
from services.models import WorkerService


class Contract(models.Model):
    # Usuario consumidor del servicio
    consumer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='consumer_contracts')

    # Servicio seleccionado por el consumidor
    service = models.ForeignKey(WorkerService, on_delete=models.CASCADE, related_name='contracts')

    # Especificaciones del trabajo solicitado
    specifications = models.TextField()

    # Notas del trabajador
    notes_worker = models.TextField(blank=True, null=True)

    # Precio actualizado después de evaluación
    price_updated = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    # Estados posibles: 'Evaluation', 'In Progress', 'Completed'
    STATUS_CHOICES = [
        ('evaluation', 'Evaluation'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='evaluation')

    # Campos adicionales para el estado 'Evaluation'
    evaluation_notes = models.TextField(blank=True, null=True)
    discount_offered = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    price_increase_reason = models.TextField(blank=True, null=True)
    # Tiempo estimado de finalización proporcionado por el trabajador
    estimated_completion_time = models.DateTimeField(blank=True, null=True)

    # Campos adicionales para el estado 'In Progress'
    start_date = models.DateField(blank=True, null=True)
    completion_date = models.DateField(blank=True, null=True)

    # Campos adicionales para el estado 'Completed'
    rating_by_consumer = models.IntegerField(blank=True, null=True)
    rating_by_worker = models.IntegerField(blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Contract ID: {self.contract_id} - {self.consumer.name} - {self.service.service.name}"

    @classmethod
    def get_filtered_contracts(cls, start_date, end_date, status):
        # Lógica para obtener contratos filtrados
        return cls.objects.filter(
            created_at__range=[start_date, end_date],
            status=status
        )
