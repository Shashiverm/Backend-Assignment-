from django.db import transaction
from .models import Loan
from customers.models import Customer

class LoanService:
    @staticmethod
    def create_loan(customer_id, loan_amount, tenure, interest_rate):
        with transaction.atomic():
            customer = Customer.objects.get(id=customer_id)
            loan = Loan.objects.create(
                customer=customer,
                loan_amount=loan_amount,
                tenure=tenure,
                interest_rate=interest_rate,
                monthly_repayment=LoanService.calculate_monthly_repayment(loan_amount, tenure, interest_rate)
            )
            return loan

    @staticmethod
    def calculate_monthly_repayment(loan_amount, tenure, interest_rate):
        monthly_interest_rate = interest_rate / 12 / 100
        number_of_payments = tenure * 12
        if monthly_interest_rate == 0:
            return loan_amount / number_of_payments
        else:
            return (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -number_of_payments)

    @staticmethod
    def get_loan_details(loan_id):
        return Loan.objects.get(id=loan_id)

    @staticmethod
    def get_customer_loans(customer_id):
        return Loan.objects.filter(customer_id=customer_id)