from django.urls import path, include

urlpatterns = [
    path('customers/', include('customers.urls')),
    path('loans/', include('loans.urls')),
]