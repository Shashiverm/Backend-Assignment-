from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Loan
from .serializers import LoanSerializer
from core.permissions import IsAuthenticated

class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        loan = self.get_object()
        serializer = self.get_serializer(loan)
        return Response(serializer.data)

    def get_queryset(self):
        customer_id = self.request.query_params.get('customer_id', None)
        if customer_id is not None:
            return self.queryset.filter(customer_id=customer_id)
        return self.queryset