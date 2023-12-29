from rest_framework import generics
from .models import Contract
from .serializers import ContractSerializer


class ContractList(generics.ListCreateAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer


class ContractDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer


class FilteredContractList(generics.ListAPIView):
    serializer_class = ContractSerializer

    def get_queryset(self):
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        status = self.request.query_params.get('status', None)
        return Contract.get_filtered_contracts(start_date, end_date, status)
