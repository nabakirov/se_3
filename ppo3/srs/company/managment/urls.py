from django.urls import path
from managment import views



urlpatterns = [
    path('payroll/', views.get_payroll_data),
]