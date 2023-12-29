from rest_framework import serializers
from .models import Contract
from services.serializers import WorkerServiceSerializer


class ContractSerializer(serializers.ModelSerializer):
    consumer = serializers.StringRelatedField()
    service = WorkerServiceSerializer()

    class Meta:
        model = Contract
        fields = '__all__'

