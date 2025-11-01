from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Loan
from customers.models import Customer

class LoanTests(APITestCase):
    def setUp(self):
        self.customer = Customer.objects.create(
            first_name="John",
            last_name="Doe",
            phone_number="1234567890",
            monthly_salary=5000,
            approved_limit=20000,
            current_debt=0
        )
        self.loan_data = {
            "loan_amount": 10000,
            "tenure": 12,
            "interest_rate": 5.0,
            "customer_id": self.customer.id
        }

    def test_create_loan(self):
        response = self.client.post(reverse('loan-create'), self.loan_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Loan.objects.count(), 1)
        self.assertEqual(Loan.objects.get().loan_amount, 10000)

    def test_view_loan_details(self):
        loan = Loan.objects.create(**self.loan_data)
        response = self.client.get(reverse('loan-detail', args=[loan.id]), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['loan_amount'], loan.loan_amount)

    def test_view_all_loans(self):
        Loan.objects.create(**self.loan_data)
        response = self.client.get(reverse('loan-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_loan_eligibility(self):
        response = self.client.post(reverse('loan-eligibility'), {"customer_id": self.customer.id, "loan_amount": 10000}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['eligible'])