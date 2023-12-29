from django.urls import path
from .views import (
    UnitOfMeasureList,
    UnitOfMeasureDetail,
    ScheduleList,
    ScheduleDetail,
    CategoryList,
    CategoryDetail,
    ServiceList,
    ServiceDetail,
    WorkerServiceList,
    WorkerServiceDetail,
    TopWorkersList, TopUsersList,
)

urlpatterns = [
    path('unit-of-measure/', UnitOfMeasureList.as_view(), name='unit-of-measure-list'),
    path('unit-of-measure/<int:pk>/', UnitOfMeasureDetail.as_view(), name='unit-of-measure-detail'),

    path('schedule/', ScheduleList.as_view(), name='schedule-list'),
    path('schedule/<int:pk>/', ScheduleDetail.as_view(), name='schedule-detail'),

    path('category/', CategoryList.as_view(), name='category-list'),
    path('category/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),

    path('service/', ServiceList.as_view(), name='service-list'),
    path('service/<int:pk>/', ServiceDetail.as_view(), name='service-detail'),

    path('worker-service/', WorkerServiceList.as_view(), name='worker-service-list'),
    path('worker-service/<int:pk>/', WorkerServiceDetail.as_view(), name='worker-service-detail'),

    path('contracts/top-workers/', TopWorkersList.as_view(), name='top-workers-list'),
    path('contracts/top-users/', TopUsersList.as_view(), name='top-users-list'),
    # Agrega otras rutas según sea necesario
]
