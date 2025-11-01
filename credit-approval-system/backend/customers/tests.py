from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Customer

class CustomerTests(APITestCase):

    def setUp(self):
        self.customer_data = {
            "first_name": "John",
            "last_name": "Doe",
            "phone_number": "1234567890",
            "monthly_salary": 5000,
            "approved_limit": 20000,
            "current_debt": 0
        }

    def test_create_customer(self):
        response = self.client.post(reverse('customer-list'), self.customer_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(Customer.objects.get().first_name, 'John')

    def test_get_customer(self):
        customer = Customer.objects.create(**self.customer_data)
        response = self.client.get(reverse('customer-detail', args=[customer.id]), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], customer.first_name)

    def test_check_loan_eligibility(self):
        customer = Customer.objects.create(**self.customer_data)
        response = self.client.post(reverse('check-loan-eligibility', args=[customer.id]), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('eligible', response.data)

    def test_view_all_customers(self):
        Customer.objects.create(**self.customer_data)
        response = self.client.get(reverse('customer-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)