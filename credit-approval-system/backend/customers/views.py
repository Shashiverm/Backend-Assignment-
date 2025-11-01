from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Customer
from .serializers import CustomerSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def check_eligibility(self, request):
        customer_id = request.data.get('customer_id')
        try:
            customer = Customer.objects.get(id=customer_id)
            # Implement eligibility logic here
            eligible = customer.monthly_salary > customer.current_debt * 0.5  # Example logic
            return Response({'eligible': eligible}, status=status.HTTP_200_OK)
        except Customer.DoesNotExist:
            return Response({'error': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['get'])
    def loans(self, request, pk=None):
        customer = self.get_object()
        loans = customer.loans.all()  # Assuming a related name 'loans' in the Customer model
        serializer = LoanSerializer(loans, many=True)  # Assuming LoanSerializer is defined
        return Response(serializer.data)