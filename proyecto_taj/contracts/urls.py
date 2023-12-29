from django.urls import path
from .views import ContractList, ContractDetail, FilteredContractList

urlpatterns = [
    path('contracts/', ContractList.as_view(), name='contract-list'),
    path('contracts/<int:pk>/', ContractDetail.as_view(), name='contract-detail'),
    path('contracts/filter/', FilteredContractList.as_view(), name='filtered-contract-list'),
    # Agrega otras rutas según sea necesario
]
