from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .form import  *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import*
# CallCenter@gmail.com
def register(request):
    return render(request, '../templates/register.html')








# def login_request(request):
#     if request.method=='POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(email=username, password=password)
#             user = User.objects.get(id=request.user.id)

#             # if user.role == "MANAGER":

#             #     login(request,user)
                
#             #     return redirect('User:manager')
            
#             # elif user.role == "EMPLOYEE":
      
#             #     login(request,user)
#             #     return redirect('User:employee')
    
#             # elif user.role == "CUSTOMER":
    
#             #     login(request,user)
#             #     return redirect( 'User:customer')
                
#             # elif user.role == "CALLCENTERMANAGER":
      
#             #     login(request,user)
#             #     return redirect('User:callcentermanager')  
            
#             # elif user.role  == "CALLCENTER":
 
#             #     login(request,user)
#             #     return redirect('User:callcenter')
                
#             # elif user.role == "MARKETING":
    
#             #     login(request,user)
#             #     return redirect('User:marketing')
            
#             # elif user.role  == "DOCTOR":
      
#             #     login(request,user)
#             #     return redirect('User:doctor')
            
#             # elif user.role == "PATIENT":
      
#             login(request,user)
#             return redirect('User:home_view')
   
#         else:
#                 messages.error(request,"Invalid username or password")
#     return render(request, '../templates/login.html',
#     context={'form':AuthenticationForm()})
 
  


def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            user = User.objects.get(id=request.user.id)
 
            login(request,user)
            return redirect('User:home_view')
   
        else:
                messages.error(request,"Invalid username or password")
    return render(request, '../templates/login.html',
    context={'form':AuthenticationForm()})
 
  

 
@login_required
def home_view(request):
    if request.user.is_authenticated:
        if request.user.is_employee():
            return redirect('User:employee')
        elif request.user.is_manager():
            return redirect('User:manager')
        elif request.user.is_callcentermanager():
            return redirect('User:CallCentermanager')
        elif request.user.is_customer():
            return redirect('User:customer')
        elif request.user.is_callCenter():
            return redirect('User:Callcenter')
        elif request.user.is_marketing():
            return redirect('User:marketing')
        elif request.user.is_doctor():
            return redirect('User:doctor')
        elif request.user.is_patient():
            return redirect('User:PATIENT')
        elif request.user.is_admin():
            return redirect('User:admin')
    return render(request, '../templates/login.html')



def home(request):
    return render(request, '../templates/Customer.html')

@login_required
 
def CallCentermanager(request):
    return render(request, '../templates/CallCenter_manager.html')
@login_required
 
def Callcenter(request):
    return render(request, '../templates/CallCenter.html')
@login_required
 
def doctor(request):
    return render(request, '../templates/Doctor.html')
@login_required
 
def manager(request):
    return render(request, '../templates/Manager.html')
@login_required
 
def marketing(request):
    return render(request, '../templates/Marketing.html')
@login_required
 
def patient(request):
    return render(request, '../templates/Patient.html')
@login_required
 
def employee(request):
    return render(request, '../templates/employee.html')
@login_required
 
def customer(request):
    return render(request, '../templates/Customer.html')
 
 
 


 




     
class customer_register(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = '../templates/customer_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('User:customer')





class employee_register(CreateView):
    model = User
    form_class = EmployeeSignUpForm
    template_name = '../templates/employee_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('User:employee')


    
class CallCenter_register(CreateView):
    model = User
    form_class = CallCenterSignUpForm
    template_name = '../templates/employee_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('User:Callcenter')
    
class Manager_register(CreateView):
    model = User
    form_class = ManagerSignUpForm
    template_name = '../templates/employee_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('User:manager')


     

# class Admin_register(CreateView):
#     model = User
#     form_class = AdminSignUpForm
#     template_name = '../templates/employee_register.html'

#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect('/')

class Marketing_register(CreateView):
    model = User
    form_class = MarketingSignUpForm
    template_name = '../templates/employee_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('User:marketing')

class CallCenter_manager_register(CreateView):
    model = User
    form_class = CallCenter_managerSignUpForm
    template_name = '../templates/employee_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('User:CallCentermanager')
class Patient_register(CreateView):
    model = User
    form_class = PatientSignUpForm
    template_name = '../templates/employee_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('User:patient') 
    
     
class Doctor_register(CreateView):
    model = User
    form_class = DoctorSignUpForm
    template_name = '../templates/employee_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('User:doctor')  
    
 
def logout_view(request):
    logout(request)
    return redirect('/')

