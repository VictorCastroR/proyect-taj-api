from rest_framework import serializers
from .models import UnitOfMeasure, Schedule, Category, Service, WorkerService
from django.contrib.auth import get_user_model

class UnitOfMeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitOfMeasure
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    staff = serializers.StringRelatedField()

    class Meta:
        model = Category
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    staff = serializers.StringRelatedField()

    class Meta:
        model = Service
        fields = '__all__'


class WorkerServiceSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    service = ServiceSerializer()

    class Meta:
        model = WorkerService
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'