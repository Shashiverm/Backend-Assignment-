from django.core.management.base import BaseCommand
import pandas as pd
from customers.models import Customer
from loans.models import Loan

class Command(BaseCommand):
    help = 'Import customer and loan data from an Excel file'

    def add_arguments(self, parser):
        parser.add_argument('excel_file', type=str, help='The path to the Excel file to import')

    def handle(self, *args, **kwargs):
        excel_file = kwargs['excel_file']
        self.import_data(excel_file)

    def import_data(self, excel_file):
        # Read the Excel file
        data = pd.read_excel(excel_file, sheet_name=None)

        # Import customers
        if 'Customers' in data:
            for index, row in data['Customers'].iterrows():
                customer, created = Customer.objects.get_or_create(
                    customer_id=row['customer_id'],
                    defaults={
                        'first_name': row['first_name'],
                        'last_name': row['last_name'],
                        'phone_number': row['phone_number'],
                        'monthly_salary': row['monthly_salary'],
                        'approved_limit': row['approved_limit'],
                        'current_debt': row['current_debt'],
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Created customer {customer.first_name} {customer.last_name}'))
                else:
                    self.stdout.write(self.style.WARNING(f'Customer {customer.first_name} {customer.last_name} already exists'))

        # Import loans
        if 'Loans' in data:
            for index, row in data['Loans'].iterrows():
                customer = Customer.objects.filter(customer_id=row['customer_id']).first()
                if customer:
                    loan = Loan(
                        loan_id=row['loan_id'],
                        loan_amount=row['loan_amount'],
                        tenure=row['tenure'],
                        interest_rate=row['interest_rate'],
                        monthly_repayment=row['monthly_repayment'],
                        customer=customer
                    )
                    loan.save()
                    self.stdout.write(self.style.SUCCESS(f'Created loan for customer {customer.first_name} {customer.last_name}'))
                else:
                    self.stdout.write(self.style.ERROR(f'Customer with ID {row["customer_id"]} not found'))