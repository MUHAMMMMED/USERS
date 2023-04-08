from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .form import  *
from django.contrib.auth.forms import AuthenticationForm
 
from .models import*

def register(request):
    return render(request, '../templates/register.html')

def home(request):
    return render(request, '../templates/Customer.html')

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

def employee(request):
    return render(request, '../templates/employee.html')
 
def customer(request):
    return render(request, '../templates/Customer.html')
 
 
 
 
 
# def home_view(request):
    
#     if request.user.is_authenticated:
#         if request.user.is_admin:
#             return redirect('accounts:manager')
#         elif request.user.is_employee:
#             return redirect('accounts:manager')
#         elif request.user.is_manager:
#             return redirect('accounts:manager')
#         elif request.user.is_callcentermanager:
#             return redirect('accounts:manager')
#         elif request.user.is_customer:
#             return redirect('accounts:manager')
#         elif request.user.is_callCenter:
#             return redirect('accounts:manager')
#         elif request.user.is_marketing:
#             return redirect('accounts:manager')
#         elif request.user.is_doctor:
#             return redirect('accounts:manager')
#         elif request.user.is_patient:
#             return redirect('accounts:manager')
#     else:
#         return render(request, '../templates/login.html')
 


 
 

def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
    
    
    # if request.method == 'POST':
    #     form = LoginForm(request.POST)
    #     if form.is_valid():
    #         email = form.cleaned_data['email']
    #         password = form.cleaned_data['password']
    #         user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                role_urls = {
                    'EMPLOYEE': 'accounts:employee',
                    'CUSTOMER':  'accounts:customer',
                    'MANAGER':  'accounts:manager',
                    'CALLCENTERMANAGER': 'accounts:callcentermanager',
                    'CALLCENTER': 'accounts:callcenter',
                    'MARKETING': 'accounts:marketing',
                    'DOCTOR': 'accounts:doctor',
                    'PATIENT': 'accounts:patient',
                }
                return redirect(role_urls.get(user.role))
            else:
                form.add_error(None, 'Invalid email or password.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# def login_request(request):
#     if request.user.is_authenticated:
#         return redirect('accounts:manager')
    
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']
#         user = authenticate(request, email=email, password=password)

#         if user is not None:
#             login(request, user)
#             role_urls = {
#                 # 'ADMIN': '/',
#                 'EMPLOYEE': 'accounts:employee',
#                 'CUSTOMER':  'accounts:customer',
#                 'MANAGER':  'accounts:manager',
#                 'CALLCENTERMANAGER': 'accounts:CallCentermanager',
#                 'CALLCENTER': 'accounts:Callcenter',
#                 'MARKETING':'accounts:marketing',
#                 'DOCTOR': 'accounts:doctor',
#                 'PATIENT': 'accounts:patient',
#             }
#             return redirect(role_urls.get(user.role))
#         else:
#             messages.error(request, 'Invalid username or password')

#     return render(request, '../templates/login.html')

 
# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             user = authenticate(request, email=email, password=password)
#             if user.role == "MANAGER":
#                 login(request, user)
#                 return redirect('/')


#             elif user.role == "EMPLOYEE":
            
 
#                 login(request,user)
#                 return redirect('/')
            
            
            
#             else:
#                 form.add_error(None, 'Invalid email or password.')
#     else:
#         form = LoginForm()
#     return render(request, 'login.html', {'form': form})
 
# from django.contrib.auth import authenticate, login
 

# def login_request(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user = authenticate(request, email=email, password=password)
#         if user is not None:
#             login(request, user)
#             if user.is_admin():
#                 return redirect('admin_home')
#             elif user.is_employee():
#                 return redirect( 'accounts:employee')
#             elif user.is_manager():
#                 return redirect('accounts:manager')
#             # Add more elif statements for each role's home page
#             else:
#                 # Handle any other roles
#                 pass
#     return render(request, 'login.html')




# def login_request(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
 
#             if user.role == "MANAGER":

#             # elid request.user.type == :
            
#             # if user is not None :
#                 login(request,user)
#                 return redirect('/')
            
#             elif user.role == "EMPLOYEE":
#         #    elif request.session.role is "Agent":
#             # elid request.user.type == :
            
#             # if user is not None :
#                 login(request,user)
#                 return redirect('/')
    
#             elif user.role == "CUSTOMER":
#         #    elif request.session.role is "Agent":
#             # elid request.user.type == :
            
#             # if user is not None :
#                 login(request,user)
#                 return redirect('/')
                
#             elif user.role == "CALLCENTERMANAGER":
#         #    elif request.session.role is "Agent":
#             # elid request.user.type == :
            
#             # if user is not None :
#                 login(request,user)
#                 return redirect('/')  
            
#             elif user.role == "CALLCENTER":
#         #    elif request.session.role is "Agent":
#             # elid request.user.type == :
            
#             # if user is not None :
#                 login(request,user)
#                 return redirect('/')
                
#             elif user.role == "MARKETING":
#         #    elif request.session.role is "Agent":
#             # elid request.user.type == :
            
#             # if user is not None :
#                 login(request,user)
#                 return redirect('/')
            
#             elif user.role == "DOCTOR":
#         #    elif request.session.role is "Agent":
#             # elid request.user.type == :
            
#             # if user is not None :
#                 login(request,user)
#                 return redirect('/')
            
#             elif user.role == "PATIENT":
#         #    elif request.session.role is "Agent":
#             # elid request.user.type == :
            
#             # if user is not None :
#                 login(request,user)
#                 return redirect('/')
            
            
#         else:
#             messages.error(request, "Invalid username or password")
#     return render(request, '../templates/login.html', context={'form': AuthenticationForm()})
 
 
 
 
 
 
 
# def login_request(request):
#     if request.method=='POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
            
#             user = User.objects.get(id=request.user.id)

#             if user.role == "MANAGER":

#             # elid request.user.type == :
            
#             # if user is not None :
#                 login(request,user)
#                 return redirect('/')
            
#             elif user.role == "EMPLOYEE":
#         #    elif request.session.role is "Agent":
#             # elid request.user.type == :
            
#             # if user is not None :
#                 login(request,user)
#                 return redirect('/')
    
#             elif user.role == "CUSTOMER":
#         #    elif request.session.role is "Agent":
#             # elid request.user.type == :
            
#             # if user is not None :
#                 login(request,user)
#                 return redirect('/')
                
#             elif user.role == "CALLCENTERMANAGER":
#         #    elif request.session.role is "Agent":
#             # elid request.user.type == :
            
#             # if user is not None :
#                 login(request,user)
#                 return redirect('/')  
            
#             elif user.role == "CALLCENTER":
#         #    elif request.session.role is "Agent":
#             # elid request.user.type == :
            
#             # if user is not None :
#                 login(request,user)
#                 return redirect('/')
                
#             elif user.role == "MARKETING":
#         #    elif request.session.role is "Agent":
#             # elid request.user.type == :
            
#             # if user is not None :
#                 login(request,user)
#                 return redirect('/')
            
#             elif user.role == "DOCTOR":
#         #    elif request.session.role is "Agent":
#             # elid request.user.type == :
            
#             # if user is not None :
#                 login(request,user)
#                 return redirect('/')
            
#             elif user.role == "PATIENT":
#         #    elif request.session.role is "Agent":
#             # elid request.user.type == :
            
#             # if user is not None :
#                 login(request,user)
#                 return redirect('/')
   
#         else:
#                 messages.error(request,"Invalid username or password")
#     return render(request, '../templates/login.html',
#     context={'form':AuthenticationForm()})


# def login_request(request):
#     if request.method=='POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
            
            
            
            
#             if user is not None :
#                 login(request,user)
#                 return redirect('accounts:home')
#             else:
#                 messages.error(request,"Invalid username or password")
                
                
                
#         else:
#                 messages.error(request,"Invalid username or password")
                
#     return render(request, '../templates/login.html',context={'form':AuthenticationForm()})
  









     
class customer_register(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = '../templates/customer_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('accounts:customer')





class employee_register(CreateView):
    model = User
    form_class = EmployeeSignUpForm
    template_name = '../templates/employee_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('accounts:employee')


    
class CallCenter_register(CreateView):
    model = User
    form_class = CallCenterSignUpForm
    template_name = '../templates/employee_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('accounts:Callcenter')
    
class Manager_register(CreateView):
    model = User
    form_class = ManagerSignUpForm
    template_name = '../templates/employee_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('accounts:manager')


     

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
        return redirect('accounts:marketing')

class CallCenter_manager_register(CreateView):
    model = User
    form_class = CallCenter_managerSignUpForm
    template_name = '../templates/employee_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('accounts:CallCentermanager')
class Patient_register(CreateView):
    model = User
    form_class = PatientSignUpForm
    template_name = '../templates/employee_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('accounts:patient') 
    
     
class Doctor_register(CreateView):
    model = User
    form_class = DoctorSignUpForm
    template_name = '../templates/employee_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('accounts:doctor')  
    
 
def logout_view(request):
    logout(request)
    return redirect('/')

