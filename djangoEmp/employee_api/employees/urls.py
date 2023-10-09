
from django.urls import path
from . import views

urlpatterns = [
    path('api/employees/', views.employee_list, name='employee-list'),
]



