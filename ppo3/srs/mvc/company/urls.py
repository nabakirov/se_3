from django.urls import path
from company import views



urlpatterns = [
    path('payroll/', views.get_payroll_data),
]