from django.urls import path
from .import  views
app_name='Accounts'

urlpatterns=[
     path('',views.register, name='register'),
     path('customer_register/',views.customer_register.as_view(), name='customerRegister'),
     path('employee_register/',views.employee_register.as_view(), name='employeeRegister'),  
     path('CallCenter_register/',views.CallCenter_register.as_view(), name='CallCenterRegister'),
     path('Manager_register/',views.Manager_register.as_view(), name='ManagerRegister'),
     path('Admin_register/',views.Admin_register.as_view(), name='AdminRegister'),
     path(' Marketing_register/',views. Marketing_register.as_view(), name='MarketingRegister'),
     path('CallCenter_manager_register/',views.CallCenter_manager_register.as_view(), name='CallCenterManagerRegister'),
     path('Patient_manager_register/',views.Patient_manager_register.as_view(), name='PatientManagerregister'),
     path('Doctor_register/',views.Doctor_register.as_view(), name='DoctorRegister'),

  
     path('login/',views.login_view, name='login'),
     # path('login/',views.login_request, name='login'),
     path('logout/',views.logout_view, name='logout'),
]
 