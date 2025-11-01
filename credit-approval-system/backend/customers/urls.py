from django.urls import path
from .views import RegisterCustomerView, CheckLoanEligibilityView, CustomerLoansView

urlpatterns = [
    path('register/', RegisterCustomerView.as_view(), name='register_customer'),
    path('eligibility/', CheckLoanEligibilityView.as_view(), name='check_loan_eligibility'),
    path('loans/', CustomerLoansView.as_view(), name='customer_loans'),
]