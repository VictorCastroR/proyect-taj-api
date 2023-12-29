from rest_framework import serializers
from .models import Rating
from contracts.serializers import ContractSerializer


class RatingSerializer(serializers.ModelSerializer):
    contract = ContractSerializer()
    worker = serializers.StringRelatedField()
    consumer = serializers.StringRelatedField()

    class Meta:
        model = Rating
        fields = '__all__'
