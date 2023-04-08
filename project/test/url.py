from django.urls import path
 
from  test.views  import *

from django.urls import path
from .views import offers_booking_view, patient_detail_view

app_name='test'

urlpatterns=[
     path('offer',offers, name='offer'),
     path('Patient',patient, name='Patient'),
     path('Booking',Booking, name='Booking'),
     path('report/',report, name='report'),
     path('Knowreport/',Knowreport, name='Knowreport'),
     
     path('offers_booking/', offers_booking_view, name='offers_booking'),
     path('offer/<int:id>',offerspageDetails, name="offerspageDetails"),
     # path('patientDetails/<int:id>',patientDetails, name="patientDetails"),
 

     path('patient/<int:id>/', patient_detail_view, name='patient_detail')


]
 
 
 
 
 
 
 