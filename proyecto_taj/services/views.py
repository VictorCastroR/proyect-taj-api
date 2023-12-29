from django.contrib.auth import get_user_model
from django.db.models import Count, Q
from rest_framework import generics
from .models import UnitOfMeasure, Schedule, Category, Service, WorkerService
from .serializers import (
    UnitOfMeasureSerializer,
    ScheduleSerializer,
    CategorySerializer,
    ServiceSerializer,
    WorkerServiceSerializer,
    UserSerializer

)


class UnitOfMeasureList(generics.ListCreateAPIView):
    queryset = UnitOfMeasure.objects.all()
    serializer_class = UnitOfMeasureSerializer


class UnitOfMeasureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UnitOfMeasure.objects.all()
    serializer_class = UnitOfMeasureSerializer


class ScheduleList(generics.ListCreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class ScheduleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ServiceList(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class WorkerServiceList(generics.ListCreateAPIView):
    queryset = WorkerService.objects.all()
    serializer_class = WorkerServiceSerializer


class WorkerServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkerService.objects.all()
    serializer_class = WorkerServiceSerializer


class TopWorkersList(generics.ListAPIView):
    serializer_class = WorkerServiceSerializer

    def get_queryset(self):
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        return WorkerService.objects.filter(contracts__status='completed').values('user').annotate(
            completed_contracts_count=Count('user')
        ).order_by('-completed_contracts_count')[:10]


class TopUsersList(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        return get_user_model().objects.annotate(
            completed_services_count=Count('user_services__contracts',
                                           filter=Q(user_services__contracts__status='completed'))
        ).order_by('-completed_services_count')[:10]
