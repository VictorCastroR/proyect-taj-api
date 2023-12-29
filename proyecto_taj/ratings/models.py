from django.db import models
from django.contrib.auth import get_user_model
from contracts.models import Contract
from django.core.exceptions import ValidationError

class Rating(models.Model):
    # Relación con el modelo Contract
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='ratings')

    def clean(self):
        """
        Validación para asegurar que solo los usuarios del contrato pueden dar calificaciones.
        """
        if self.consumer not in [self.contract.consumer, self.contract.worker]:
            raise ValidationError("El consumidor no está vinculado al contrato.")
        if self.worker not in [self.contract.consumer, self.contract.worker]:
            raise ValidationError("El trabajador no está vinculado al contrato.")

    # Usuario que recibe la calificación (trabajador)
    worker = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='received_ratings')

    # Información del consumidor
    consumer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='given_ratings')

    # Calificación dada por el consumidor
    consumer_score = models.IntegerField()

    # Comentario del consumidor
    consumer_comment = models.TextField(blank=True, null=True)

    # Fotos en formato Base64 para el consumidor (hasta tres)
    consumer_photo1 = models.TextField(blank=True, null=True)
    consumer_photo2 = models.TextField(blank=True, null=True)
    consumer_photo3 = models.TextField(blank=True, null=True)

    # Información del trabajador

    # Calificación dada al trabajador
    worker_score = models.IntegerField()

    # Comentario del trabajador
    worker_comment = models.TextField(blank=True, null=True)

    # Fotos en formato Base64 para el trabajador (hasta tres)
    worker_photo1 = models.TextField(blank=True, null=True)
    worker_photo2 = models.TextField(blank=True, null=True)
    worker_photo3 = models.TextField(blank=True, null=True)

    # Estado de revisión de la calificación
    reviewed = models.BooleanField(default=False)

    # Staff que revisó la calificación
    reviewed_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name='reviewed_ratings')
    # Fecha de creación del rating
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rating from {self.consumer.name} to {self.worker.name}"
