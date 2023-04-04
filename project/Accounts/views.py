 
from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .form import *
from django.contrib.auth.forms import AuthenticationForm
from Accounts.models import *



def register(request):
    return render(request, '../templates/index.html')
 



 



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
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid credentials. Please try again.'
    
    return render(request, '../templates/login.html', {'error_message': error_message})

















def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('/')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, '../templates/login.html',
    context={'form':AuthenticationForm()})






def logout_view(request):
    logout(request)
    return redirect('/')

 




class employee_register(CreateView):
    model = User
    form_class = EmployeeSignUpForm
    template_name = '../templates/employee_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')



class Manager_register(CreateView):
    model = User
    form_class = ManagerSignUpForm
    template_name = '../templates/employee_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')
 

    
    
class Admin_register(CreateView):
    model = User
    form_class = AdminSignUpForm
    template_name = '../templates/employee_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class Marketing_register(CreateView):
    model = User
    form_class = MarketingSignUpForm
    template_name = '../templates/employee_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/') 

class CallCenter_register(CreateView):
    model = User
    form_class = CallCenterSignUpForm
    template_name = '../templates/employee_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')  

class CallCenter_manager_register(CreateView):
    model = User
    form_class = CallCenter_managerSignUpForm
    template_name = '../templates/employee_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

    
    
class Patient_manager_register(CreateView):
    model = User
    form_class = PatientSignUpForm
    template_name = '../templates/employee_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')
    

 
    

class customer_register(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = '../templates/customer_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class Doctor_register(CreateView):
    model = User
    form_class = DoctorSignUpForm
    template_name = '../templates/customer_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')
    
 
    
    
 