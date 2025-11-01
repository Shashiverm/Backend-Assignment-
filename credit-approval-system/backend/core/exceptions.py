class CustomException(Exception):
    """Base class for custom exceptions in the application."""
    pass

class CustomerNotFoundException(CustomException):
    """Exception raised when a customer is not found."""
    def __init__(self, customer_id):
        self.message = f"Customer with ID {customer_id} not found."
        super().__init__(self.message)

class LoanNotFoundException(CustomException):
    """Exception raised when a loan is not found."""
    def __init__(self, loan_id):
        self.message = f"Loan with ID {loan_id} not found."
        super().__init__(self.message)

class InvalidLoanAmountException(CustomException):
    """Exception raised for invalid loan amounts."""
    def __init__(self, amount):
        self.message = f"Invalid loan amount: {amount}. It must be greater than zero."
        super().__init__(self.message)

class EligibilityCheckException(CustomException):
    """Exception raised when eligibility check fails."""
    def __init__(self, reason):
        self.message = f"Eligibility check failed: {reason}."
        super().__init__(self.message)