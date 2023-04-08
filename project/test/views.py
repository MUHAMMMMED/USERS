from django.shortcuts import render, get_object_or_404, redirect
from Accounts.models import *
# Create your views here.
from django.shortcuts import render
from django.http import Http404
from django.utils.text import slugify
from .forms import *
# from django.shortcuts import render , redirect
from test.models  import *
from test.Calendar import *
# # Create your views here.OfersBookingform

from django.contrib.auth.decorators import login_required
from Accounts.models import *


def offers(request):
    offer = Offers.objects.all()
    context = { 'offer':offer, } 
    return render(request, 'offer.html', context)



def patient(request):
    PatientS = PATIENT.objects.all()
    
    context = { 'PatientS':PatientS,} 
    return render(request, 'patient.html', context)


# +++++++++++++++++++++++++++++++++++


@login_required(login_url='login')

# def Booking(request):
 
#     user = User.objects.get(id=request.user.id)

#     if user.role == "CallCenter":

#      booking = OffersBooking.objects.filtter(user=user)


#      context = { 'booking':booking,} 
#      return render(request, 'booking.html', context)
 
# def Booking(request):
#     try:
#         user = User.objects.get(id=request.user.id)
#     except User.DoesNotExist:
#         user = None

#     if user and user.role == User.Role.CALLCENTER:
#         booking = OffersBooking.objects.filter(user=user)
#         context = {'booking': booking}
#         return render(request, 'booking.html', context)
#     else:
#         return HttpResponse('Unauthorized', status=401)
    
    
# def Booking(request):
#     user = request.user
#     booking = OffersBooking.objects.filter(CALLCENTER__user=user)
#     context = {'booking': booking}
#     return render(request, 'booking.html', context)
    
 
def Booking(request):
    # Get the current user's CallCenter object
    # callcenter = request.user.callcenter
    callcenter = User.objects.get(id=request.user.id)

    # Filter the OffersBooking objects by the current user's CallCenter
    bookings = OffersBooking.objects.filter(Callcenter=callcenter)

    context = {'booking': bookings}
    return render(request, 'booking.html', context)


 

# def Booking(request):
#     # Get the current user's CallCenter object
#     callcenter = get_object_or_404(CallCenter, user=request.user)
 
#     # Filter the OffersBooking objects by the current user's CallCenter
#     bookings = OffersBooking.objects.filter(Callcenter=callcenter)

#     context = {'booking': booking}
#     return render(request, 'booking.html', context)
 


# +++++++++++++++++++++++++++++++++++
 
 
 
 
@login_required(login_url='login')
def offers_booking_view(request):

    offers_booking_data = OffersBooking.objects.all()
    context ={'offers_booking_data': offers_booking_data} 

    return render(request, 'offers_booking.html',context  )
        
def offerspageDetails(request, id):
    offeR = get_object_or_404(Offers, id=id)


    if request.method == 'POST':
        form = OfersBookingform(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.offer = offeR
            booking.save()
            print('Done')
            name = form.cleaned_data['name']
            number = form.cleaned_data['phone_number']
            print('number', number)

            try:
                obj, created = PATIENT.objects.get_or_create(phone_number=number, defaults={'name': name})
                if created:
                    print('Create New PATIENT')
                else:
                    print('PATIENT already exists')
                booking.patients = obj
                booking.save()
                print('SAVE booking IN PATIENT')

            except IntegrityError:
                print("UNIQUE constraint failed: test_patient.phone_number")
        else:
            print('Form is not valid')
            print('404')
    else:
        form = OfersBookingform()
        print('404')

    context = {'offer': offeR, 'form': form}
    return render(request, 'offerdetails.html', context)


@login_required(login_url='login')
def patient_detail_view(request,id):
    patient_data = get_object_or_404(PATIENT, id=id)
    context={'patient_data': patient_data}
    return render(request, 'patient_detail.html', context)

















from datetime import datetime
from datetime import datetime, timedelta
from django.shortcuts import render
from .models import PATIENT, OffersBooking
from django.db.models import Count



from datetime import datetime, timedelta


@login_required(login_url='login')
def report(request):
    # Get start and end dates from query parameters
    # start_date_str = request.GET.get('start_date')
    # end_date_str = request.GET.get('end_date')
    start_date_str = '2023-04-06'
    end_date_str = '2023-04-06' 
    # Convert start and end dates to datetime objects if they are not None
    if start_date_str:
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    else:
        start_date = datetime.now().date()
    
    if end_date_str:
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d') + timedelta(days=1)
    else:
        end_date = datetime.now().date() + timedelta(days=1)
    
    # Get counts of patients, offers bookings, and phone numbers
    patient_count = PATIENT.objects.filter(date_joined__gte=start_date, date_joined__lte=end_date).count()

    booking_count = OffersBooking.objects.filter(date__gte=start_date, date__lte=end_date).count()

    # phone_count = OffersBooking.objects.filter(created_at__gte=start_date, created_at__lte=end_date).distinct('phone_number').count()
    phone_count = OffersBooking.objects.filter(date__gte=start_date, date__lte=end_date).values('phone_number').annotate(count=Count('phone_number')).count()
    print('404')
    context = {
        'start_date': start_date_str,
        'end_date': end_date_str,
        'patient_count': patient_count,
        'booking_count': booking_count,
        'phone_count': phone_count,
    }
    
    return render(request, 'report.html', context)

 
# from django.db.models import Count
# from django.shortcuts import render
 
 
# def Knowreport(request):
#     # Get start and end dates from query parameters
#     # start_date_str = request.GET.get('start_date')
#     # end_date_str = request.GET.get('end_date')
#     start_date_str = '2023-04-06'
#     end_date_str = '2023-04-06' 
#     # Convert start and end dates to datetime objects if they are not None
#     if start_date_str:
#         start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
#     else:
#         start_date = datetime.now().date()
 
#     if end_date_str:
#         end_date = datetime.strptime(end_date_str, '%Y-%m-%d') + timedelta(days=1)
#     else:
#         end_date = datetime.now().date() + timedelta(days=1)
 
#     # Get counts of each value in the Know model for the specified period
#     count_by_title = Knew.objects.filter(date__gte=start_date, date__lte=end_date).values('title').annotate(count=Count('id'))
 
#     context = {
#         'start_date': start_date_str,
#         'end_date': end_date_str,
#         'count_by_title': count_by_title,
#     }
 
#     return render(request, 'Knowreport.html', context)







 


# class Calendar(HTMLCalendar):
#     def __init__(self, know):
#         super().__init__()
#         self.know = self.group_by_day(know)

#     def formatday(self, day, weekday):
#         if day != 0:
#             cssclass = self.cssclasses[weekday]
#             if datetime.now().date() == datetime(self.year, self.month, day).date():
#                 cssclass += ' today'
#             if day in self.know:
#                 cssclass += ' filled'
#                 body = []
#                 for item in self.know[day]:
#                     body.append(f'<li>{item.title}</li>')
#                 return f"<td class='{cssclass}'><span class='date'>{day}</span><ul>{''.join(body)}</ul></td>"
#             return f"<td class='{cssclass}'><span class='date'>{day}</span></td>"
#         return '<td class="noday">&nbsp;</td>'

#     def formatweek(self, theweek):
#         s = ''.join(self.formatday(d, wd) for (d, wd) in theweek)
#         return f'<tr>{s}</tr>'



#     def formatmonth(self, year, month, withyear=True):
#         self.year, self.month = year, month
#         v = []
#         a = v.append
#         a('<table class="calendar">')
#         a('\n')
#         a(self.formatmonthname(year, month, withyear=withyear))
#         a('\n')
#         a(self.formatweekheader())
#         a('\n')
#         for week in self.monthdays2calendar(year, month):
#             a(self.formatweek(week))
#             a('\n')
#         a('</table>')
#         a('\n')
#         return mark_safe(''.join(v))

#     def group_by_day(self, know):
#         field = lambda know: know.date.day
#         return dict(
#             [(day, list(items)) for day, items in groupby(know, field)]
#         )
# from django.db.models import Count
# from django.shortcuts import render, get_object_or_404
# from django.utils.safestring import mark_safe
# from django.http import HttpResponse
# from .models import Know
# from itertools import groupby
# from calendar import HTMLCalendar
# from datetime import datetime, timedelta
# from reportlab.pdfgen import canvas

# def Knowreport(request):
#     # Get start and end dates from query parameters
#     start_date_str = request.GET.get('start_date')
#     end_date_str = request.GET.get('end_date')

#     # Convert start and end dates to datetime objects if they are not None
#     if start_date_str:
#         start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
#     else:
#         start_date = datetime.now().date()

#     if end_date_str:
#         end_date = datetime.strptime(end_date_str, '%Y-%m-%d') + timedelta(days=1)
#     else:
#         end_date = datetime.now().date() + timedelta(days=1)

#     # Get counts of each value in the Know model for the specified period
#     know = Knew.objects.filter(date__gte=start_date, date__lte=end_date).order_by('date')

#     count_by_title = know.values('title').annotate(count=Count('id'))

#     calendar = Calendar(know).formatmonth(int(start_date.strftime('%Y')), int(start_date.strftime('%m')))

#     context = {
#         'start_date': start_date_str,
#         'end_date': end_date_str,
#         'count_by_title': count_by_title,
#         'calendar': calendar,
#     }
#     # Handle PDF export button click
#     if 'export_pdf' in request.GET:
#         response = HttpResponse(content_type='application/pdf')
#         response['Content-Disposition'] = f'attachment; filename="report_{start_date_str}_{end_date_str}.pdf"'

#         # Generate PDF file
#         p = canvas.Canvas(response)
#         p.drawString(100, 800, f"Report for {start_date_str} to {end_date_str}")
#         y = 750
#         for item in count_by_title:
#             p.drawString(100, y, f"{item['title']}: {item['count']}")
#             y -= 20
#         p.showPage()
#         p.save()

#         return response

#     return render(request, 'Knowreport.html', context)





from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.utils.safestring import mark_safe
from django.http import HttpResponse
 
from itertools import groupby
from calendar import HTMLCalendar
from datetime import datetime, timedelta
from reportlab.pdfgen import canvas

 
def Knowreport(request):
    # Get start and end dates from query parameters
    start_date_str = request.GET.get('start_date')
    end_date_str = request.GET.get('end_date')

    # Convert start and end dates to datetime objects if they are not None
    if start_date_str:
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    else:
        start_date = datetime.now().date()

    if end_date_str:
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d') + timedelta(days=1)
    else:
        end_date = datetime.now().date() + timedelta(days=1)

    # Get counts of each value in the Know model for the specified period
    know = Knew.objects.filter(date__gte=start_date, date__lte=end_date).order_by('date')
    count_by_title = know.values('title').annotate(count=Count('id'))
    calendar = Calendar(know).formatmonth(int(start_date.strftime('%Y')), int(start_date.strftime('%m')))





    # # Handle PDF export button click
    # if 'export_pdf' in request.POST:
    #     # Create a PDF file with the report data
    #     response = HttpResponse(content_type='application/pdf')
    #     response['Content-Disposition'] = f'attachment; filename="report_{start_date_str}_{end_date_str}.pdf"'

    #     p = canvas.Canvas(response)
    #     p.drawString(100, 800, f"Report for {start_date_str} to {end_date_str}")
    #     y = 750
    #     for item in count_by_title:
    #         p.drawString(100, y, f"{item['title']}: {item['count']}")
    #         y -= 20
    #     p.showPage()
    #     p.save()

    #     return response

  # Handle PDF export
    if 'export_pdf' in request.GET:
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="report_{start_date}_{end_date}.pdf"'

        # Create the PDF document using ReportLab
        p = canvas.Canvas(response)
        p.drawString(100, 800, f"Report for {start_date} to {end_date}")
        # ... code to add report data to PDF ...

        p.showPage()
        p.save()







    context = {
        'start_date': start_date_str,
        'end_date': end_date_str,
        'count_by_title': count_by_title,
        'calendar': calendar,

    }







    return render(request, 'Knowreport.html', context)
 
from django.urls import reverse
 
 
# def offerspageDetails(request, id):
#     offer = get_object_or_404(Offers, id=id)
#     if request.method == 'POST':
#             form = OfersBookingform(request.POST)
#         # if form.is_valid():
#             booking = form.save(commit=False)
#             booking.name = request.POST.get('name')
#             booking.phone = request.POST.get('phone')
#             booking.Message = request.POST.get('Message')
#             booking.offer = offer
#             print('Done',booking)
#             booking.save()
#             print('Done')
#     else:
#         form = OfersBookingform()
#         print('404')
    
#     context = {'offer': offer, 'form': form}
#     return render(request, 'offerdetails.html', context)




 

# def offerspageDetails(request, id):
#         offeR = get_object_or_404(Offers, id=id)

#         if request.method == 'POST':
#                 form = OfersBookingform(request.POST)
#                 if form.is_valid():
#                           booking = form.save(commit=False)
#                           # booking.name = request.POST.get('name')
#                           # print('Done',booking)
#                           # booking.phone_number = request.POST.get('phone_number')
#                           # print('Done',booking)
#                           # booking.Message = request.POST.get('Message')
#                           # print('Done',booking)
#                           booking.offer = offeR
#                           booking.save()
#                           print('Done')
#                           name=booking.name
#                           number=booking.phone_number
#                           print('number',number)

#                           try:

#                             if PATIENT.objects.filter(phone_number='number').exists() == False:
                               
#                                  print('exists-NO' )
#                                  obj=PATIENT.objects.create(name=name, phone_number = number,) 
#                                  obj.save()
#                                  print('Create New PATIENT ')
#                                  booking.patients =obj
#                                  booking.save()
#                                  print('SAVE booking IN PATIENT ')

#                             else:

#                              print('exists-YES' )
   
#                              if PATIENT.objects.filter(phone_number='number').exists() == True:

#                                 print('exists-True' )

#                           except:
#                                 print("UNIQUE constraint failed: test_patient.phone_number")


#                 else:
#                      print('Form is not valid')
#                      print('404')




#         else:
 
#                     form = OfersBookingform()
#                     print('PATIENT404')
 
#         context = {'offer': offeR,'form':form }
#         return render(request, 'offerdetails.html', context)


# request.POST['id']


# def offerspageDetails(request, id):
#     offeR = get_object_or_404(Offers, id=id)
#     phone_number = request.GET.get('phone_number')
#     # # phonE = request.POST.get('phone')
#     # print('Done',phone_number)
#     CC=PATIENT.objects.filter(phone_number='phone_number').exists()
#     print('exists',CC)

#     if PATIENT.objects.filter(phone_number='phone_number').exists():

#             print('yes')

#             if request.method == 'POST':
#                 form = OfersBookingform(request.POST)
#                 if form.is_valid():
#                      booking = form.save(commit=False)
#                      # booking.name = request.POST.get('name')
#                      # print('Done',booking)
#                      # booking.phone_number = request.POST.get('phone_number')
#                      # print('Done',booking)
#                      # booking.Message = request.POST.get('Message')
#                      # print('Done',booking)
#                      # booking.offer = offeR
#                      # print('Done',booking)
#                      booking.save()
#                      print('Done')
#                 else:
#                      print('Form is not valid')
#                      print('404')




#     else:

#            if request.method == 'POST':
#                      print('NO')
#                      form = PATIENTform(request.POST)
#                      if form.is_valid():
#                         name = request.POST.get('name')
#                         phone_number = request.POST.get('phone_number')
#                         obj=PATIENT.objects.create( name=name, phone_number = phone_number,  ) 
#                         obj.save()
#                      else:
#                        print('UNIQUE phone_number')
                     
#                 # form = PATIENTform()  

#                 # if form.is_valid():
#                 #      bookingg = form.save(commit=False)

#                      # booking = PATIENTform()  
                    
#                      # booking.name = request.POST.get('name')
#                      # print('Done',booking)
#                      # booking.phone = request.POST.get('phone')
#                      # print('Done',booking)
#                      # booking.save()
#                      # print('Done')

#                      if request.method == 'POST':
#                            form = OfersBookingform(request.POST)
#                            if form.is_valid():
#                                booking = form.save(commit=False)
#                                # booking.name = request.POST.get('name')
#                                # print('Done',booking)
#                                # booking.phone = request.POST.get('phone')
#                                # print('Done',booking)
#                                # booking.Message = request.POST.get('Message')
#                                # print('Done',booking)
#                                # booking.offer = offeR
#                                # print('Done',booking)

#                                booking.save()
#                                print('Done2')
#                            else:
#                             print('Form is not valid')
#                             print('404.OfersBookingform 2')
#                      else:
#                        print('404OPATIENTform')
#                        form = OfersBookingform()



#            else:
#                     form = OfersBookingform()
#                     print('PATIENT404')
 
#     context = {'offer': offeR,'form':form }
#     return render(request, 'offerdetails.html', context)



# def validate_phone_number(request):
#     phone_number = request.GET.get('phone_number', '')  # Get the phone number from the request

#     try:
#         parsed_number = phonenumbers.parse(phone_number, None)
#         if phonenumbers.is_valid_number(parsed_number):
#             return JsonResponse({"valid": True, "message": "Valid phone number."})
#         else:
#             return JsonResponse({"valid": False, "message": "Invalid phone number."})
#     except phonenumbers.NumberParseException as e:
#         return JsonResponse({"valid": False, "message": "Invalid phone number."})
 







# Create a function to check the phone number format:
# def is_valid_indian_phone_number(phone_number):
#     # Indian phone numbers can start with +91 or 0
#     # followed by a 10-digit number (where the first digit is between 7 and 9)
#     pattern = re.compile(r'(?:\+91|0)[7-9]\d{9}')
#     return bool(pattern.fullmatch(phone_number))




 

# 'form': form

# def offerspageDetails(request, id):
#     offer = get_object_or_404(Offers, id=id)
#     if request.method == 'POST':
#         form = OfersBookingform(request.POST)
#         if form.is_valid():
#             booking = form.save(commit=False)
#             Name =request.POST.get('name')
#             booking.name=Name
 
#             Phone = request.POST.get('phone')
#             booking.phone=Phone

#             MessaGe = request.POST.get('Message')
#             booking.phone=MessaGe

#             booking.offer=Offer


#             booking=OffersBooking(booking)


 
#             booking.save()
#             print('Done')
#     else:
#         form = OfersBookingform()
#         print('404')
    
#     context = {'offer': offer,  }
#     return render(request, 'offerdetails.html', context)


# def offerspageDetails(request, id):
#    Offer = get_object_or_404(Offers,id=id,)
 

#     # form= OfersBookingform(request.POST)

#     # if request.method == 'POST':

#     #     form = OfersBookingform(request.POST)
#     #     if form.is_valid():
#     #       myform = form.save(commit=False)

#     #       Name =request.POST.get('name')
#     #       myform.name=Name
 
#     #       Phone = request.POST.get('phone')
#     #       myform.phone=Phone

#     #       MessaGe = request.POST.get('Message')
#     #       myform.phone=MessaGe

#     #       myform.offer=Offer
#     #       yform=OffersBooking(myform)
#     #       yform.save()
         
#     #       print('DOne')  
  
#    # form = OfersBookingform(request.POST or None)
#    # if request.POST and form.is_valid():

#    #      Name = form.cleaned_data['name']
#    #      Phone = form.cleaned_data['phone']
#    #      MessaGe = form.cleaned_data['Message']
        



#    #      obj = OffersBooking(
#    #          name=Name, 
#    #          phone = Phone, 
#    #          Message = MessaGe,
#    #          offer=Offer,
#    #      )


#    # obj.save()


#     # form= OfersBookingform(request.POST)

#     # if request.method == 'POST':


#    # if(request.method == "POST"):
#    #      form = OfersBookingform(request.POST)

#    #      if form.is_valid():
#    #          obj = form.save(commit = False)
#    #          Name =request.POST.get('name')
#    #        # myform.name=Name
#    #          Phone = request.POST.get('phone')
#    #        # myform.phone=Phone
#    #          MessaGe = request.POST.get('Message')

#    #          obj=OffersBooking.objects.create(
#    #          name=Name, 
#    #          phone = Phone, 
#    #          Message = MessaGe,
#    #          offer=Offer,
#    #          # patients=
#    #          )
#    #          obj.save()
      

#    if request.method=='POST':
#         form = OfersBookingform(request.POST)
#         # if entered values are good pass it to database
#         if form.is_valid():



#             form.name=request.POST['name'],
#             form.phone=request.POST['phone'],
#             form.Message=request.POST['Message'],
#                 # name = form.cleaned_data['name']
#                 # phone = form.cleaned_data['phone']
#                 # Message = form.cleaned_data['Message']
#             form.offer=Offer,
                                
#             form.save() 
#             print('DOne') 












#           # myform.phone=MessaGe

#           # myform.offer=Offer
     

#    # return redirect("home")
#    else:
               
#         form = OfersBookingform()
#         print('404')  
 
         
#    context = {
#          'offer':Offer,
#          # 'form':form
#       }      
   
 

#    return render(request, 'offerdetails.html', context)




@login_required(login_url='login')
def patientDetails(request, id):
    patients = get_object_or_404(PATIENT,id=id,)
 
 
    context = {
         'patients':patients 
          
    } 
 
      
              
    

    return render(request, 'patientdetails.html', context)
  

# phone_number


# class RecipeForm(forms.ModelForm):
#     error_css_class = 'error-field'
#     required_css_class = 'required-field'
#     name = forms.CharField(help_text='This is your help! <a href="/contact">Contact us</a>')
#     # descriptions = forms.CharField(widget=forms.Textarea(attrs={"rows": 3}))
#     class Meta:
#         model = Recipe
#         fields = ['name', 'description', 'directions']
    
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # django-crispy-forms
#         for field in self.fields:
#             new_data = {
#                 "placeholder": f'Recipe {str(field)}',
#                 "class": 'form-control',
#                 # "hx-post": ".",
#                 # "hx-trigger": "keyup changed delay:500ms",
#                 # "hx-target": "#recipe-container",
#                 # "hx-swap": "outerHTML"
#             }
#             self.fields[str(field)].widget.attrs.update(
#                 new_data
#             )
#         # self.fields['name'].label = ''
#         # self.fields['name'].widget.attrs.update({'class': 'form-control-2'})
#         self.fields['description'].widget.attrs.update({'rows': '2'})
#         self.fields['directions'].widget.attrs.update({'rows': '4'})


# class RecipeIngredientForm(forms.ModelForm):
#     class Meta:
#         model = RecipeIngredient
#         fields = ['name', 'quantity', 'unit']


 















    # if request.method == 'POST': 
    #    ddoctor = Doctor.objects.all()  
    #    print('000000000000',ddoctor)
    #    User=request.user 
    #    startdate =request.POST.get('start')
    #    print('start :',startdate) 
    #    enddate = request.POST.get('end')
    #    print('end :',enddate) 

    #    doctor=request.POST.get('secretdoctor')
    #    print('doctor :',doctor) 

    #    Sample=OffersBooking.objects.filter(datefilter__range=[startdate,enddate],user=User)  
    #    visit   = Sample.filter(status='حضر').count
    #    print('Sample :',Sample) 
    # #    visitt=visit.tolist.values()

    # #     data = OffersBooking.objects.all()
    # # data_df = pd.DataFrame(data)
    # # data_df1=data_df[["amount","status"]]
    # # total_df = data_df1.query('status == "حضر"')
    # # amount1=total_df ["amount"].astype(int).sum()
    # # amount=amount1.tolist()

    # #    print('visit',visitt)
    #    print('visit',visit)
    # #    doctorr=OffersBooking.objects.filter(doctor__title__contains="trfujrtfhj") 






#                         <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
#                         <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
#                         <script src="https://unpkg.com/gijgo@1.9.14/js/gijgo.min.js" type="text/javascript"></script>
#                         <link href="https://unpkg.com/gijgo@1.9.14/css/gijgo.min.css" rel="stylesheet" type="text/css" />
              




              
#                         <div class="d-flex justify-content-center">
#                             <form action = "" method = "POST">  {% csrf_token %}  
#                              <div class="form-group mb-2"> <input id="datepicker0"  'type': 'date'    name="start"  data-provide="datepicker"  data-date-format="%d/%m/%Y" placeholder="start date" required  style="text-align:center;"/></div>
#                                   <h5 class="text-center"> TO </h5>   
#                              <div class="form-group  mb-2"> <input id="datepicker" 'type': 'date'    name="end"  data-provide="datepicker"  data-date-format="%d/%m/%Y" placeholder="end date" required   style="text-align:center;"/> </div>

 

#                             <button type="submit" class="btn btn-primary mb-2">sand</button></div>
# <select class="form-select form-select-lg mb-3"  id="secretdoctor" name="secretdoctor">
 
#   <option selected>Open this select menu</option>
#     {% for doctor in doctor %}
#   <option value="{{doctor.id}}">{{doctor.title}}</option>
#    {% endfor %}
# </select>

#                           </form>
#                         </div>












# if Entry.objects.filter(pk=1).exists():
#     # …
# else:
#     # …




























                        # <script>




 
                        #     $("#from-datepicker").datepicker({});
 
                        #   $('#datepicker').datepicker({
                        #         uiLibrary: 'bootstrap4',format: 'yyyy-mm-dd'
                        #     });  
                        #     $('#datepicker0').datepicker({
                        #         uiLibrary: 'bootstrap4',format: 'yyyy-mm-dd'
                        #     } );   
                        #     {% comment %} $.fn.datepicker.defaults.format = 'yy-mm-dd'; {% endcomment %}
                        #     {% comment %} $.fn.datepicker.defaults.format = 'yy-mm-dd';
                            
                        #     $("#from-datepicker").datepicker({format: 'yy-mm-dd'});

                        #     $(function(){
                        #         $("#to").datepicker({ dateFormat: 'yy-mm-dd' });
                        #         $("#from").datepicker({ dateFormat: 'yy-mm-dd' }).bind("change",function(){
                        #             var minValue = $(this).val();
                        #             minValue = $.datepicker.parseDate("yy-mm-dd", minValue);
                        #             minValue.setDate(minValue.getDate()+1);
                        #             $("#to").datepicker( "option", "minDate", minValue );
                        #         })
                        #     }); {% endcomment %}
                         
                        # </script>

 