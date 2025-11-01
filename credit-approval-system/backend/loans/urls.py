from django.urls import path
from .views import LoanCreateView, LoanDetailView, LoanListView, CheckLoanEligibilityView

urlpatterns = [
    path('loans/', LoanListView.as_view(), name='loan-list'),
    path('loans/create/', LoanCreateView.as_view(), name='loan-create'),
    path('loans/<int:pk>/', LoanDetailView.as_view(), name='loan-detail'),
    path('loans/eligibility/', CheckLoanEligibilityView.as_view(), name='check-loan-eligibility'),
]