 
from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .form import *
from django.contrib.auth.forms import AuthenticationForm
from Accounts.models import *



def home(request):
    return render(request, '../templates/index.html')
 
def CallCentermanager(request):
    return render(request, '../templates/CallCenter_manager.html')

def Callcenter(request):
    return render(request, '../templates/CallCenter.html')

def doctor(request):
    return render(request, '../templates/Doctor.html')

def manager(request):
    return render(request, '../templates/Manager.html')

def marketing(request):
    return render(request, '../templates/Marketing.html')

def patient(request):
    return render(request, '../templates/Patient.html')

def customer(request):
    return render(request, '../templates/Customer.html')

def admin(request):
    return render(request, '../templates/Admin.html')
 
def employee(request):
    return render(request, '../templates/employee.html')
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):

    if request.method == 'POST':
        username_or_email = request.POST.get('username_or_email')
        password = request.POST.get('password')
        
        # Check if the user entered their email or username
        if '@' in username_or_email:
            # User entered email, so authenticate with email
            user = authenticate(request, email=username_or_email, password=password)
        else:
            # User entered username, so authenticate with username
            user = authenticate(request, username=username_or_email, password=password)
            
        if user and user.is_admin is False:
 
   
           login(request, user)
           return redirect('home')  
       
        elif user and user.is_manager is True:
           login(request, user)
           return redirect('accounts:manager')  
       
        elif user and user.is_CallCenter_manager is True: 
           login(request, user)
           return redirect('accounts:CallCentermanager')  
       
        elif user and user.is_marketing is True:  
           login(request, user)
           return redirect('accounts:marketing')  
        
        elif user and user.is_CallCenter is True:  
           login(request, user)
           return redirect('accounts:Callcenter')  
   
        elif user and user.is_patient is True: 
           login(request, user)
           return redirect('accounts:patient')  
        
        elif user and user.is_doctor is True: 
           login(request, user)
           return redirect('accounts:doctor') 
        
        elif user and user.is_customer is True: 
           login(request, user)
           return redirect('accounts:customer')  
        
        elif user and user.is_employee is True: 
           login(request, user)
           return redirect('accounts:employee')  
            

      
        else:
            error_message = 'Invalid credentials. Please try again.'
    
    return render(request, '../templates/login.html', {'error_message': error_message})

 





 




class employee_register(CreateView):
    model = User
    form_class = EmployeeSignUpForm
    template_name = '../templates/employee_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('accounts:customer')  



class Manager_register(CreateView):
    model = User
    form_class = ManagerSignUpForm
    template_name = '../templates/employee_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('accounts:manager')  
 

    
    
class Admin_register(CreateView):
    model = User
    form_class = AdminSignUpForm
    template_name = '../templates/employee_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('accounts:admin')  

class Marketing_register(CreateView):
    model = User
    form_class = MarketingSignUpForm
    template_name = '../templates/employee_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('accounts:marketing') 

class CallCenter_register(CreateView):
    model = User
    form_class = CallCenterSignUpForm
    template_name = '../templates/employee_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('accounts:Callcenter')  
          
class CallCenter_manager_register(CreateView):
    model = User
    form_class = CallCenter_managerSignUpForm
    template_name = '../templates/employee_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('accounts:CallCentermanager') 

    
    
class Patient_manager_register(CreateView):
    model = User
    form_class = PatientSignUpForm
    template_name = '../templates/employee_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('accounts:patient') 
    

 
    

class customer_register(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = '../templates/customer_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('accounts:customer') 

class Doctor_register(CreateView):
    model = User
    form_class = DoctorSignUpForm
    template_name = '../templates/customer_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('accounts:doctor') 
    
 
 
 
 
 
            

def logout_view(request):
    logout(request)
    return redirect('/')
 
   
                
     

        
 