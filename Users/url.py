from django.urls import path
from .views import*
app_name='Users'

urlpatterns=[
     
     path('',register, name='home'),
     path('home_view',home_view, name='home_view'),

     
     
     path('CallCentermanager',CallCentermanager, name='CallCentermanager'),
     path('Callcenter',Callcenter, name='Callcenter'),
     path('doctor',doctor, name='doctor'),
     path('manager',manager, name='manager'),
     path('marketing',marketing, name='marketing'),
     path('patient',patient, name='patient'),
     path('customer',customer, name='customer'),
    #  path('admin',views.admin, name='admin'), 
     path('employee',employee, name='employee'), 
     path('home',home, name='home'), 
  
     path('customer_register/',customer_register.as_view(), name='customerRegister'),
     path('employee_register/',employee_register.as_view(), name='employeeRegister'),  
     path('CallCenter_register/',CallCenter_register.as_view(), name='CallCenterRegister'),
     path('Manager_register/',Manager_register.as_view(), name='ManagerRegister'),
    #  path('Admin_register/',Admin_register.as_view(), name='AdminRegister'),
     path(' Marketing_register/',Marketing_register.as_view(), name='MarketingRegister'),
     path('CallCenter_manager_register/',CallCenter_manager_register.as_view(), name='CallCenterManagerRegister'),
     path('Patient_register/',Patient_register.as_view(), name='Patientregister'),
     path('Doctor_register/',Doctor_register.as_view(), name='DoctorRegister'),

 
 
     path('login/',login_request, name='login'),
     path('logout/',logout_view, name='logout'),
]
 
 