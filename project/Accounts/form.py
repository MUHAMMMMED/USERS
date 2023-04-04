
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from Accounts.models import *


# from django import forms
# from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# from .models import CustomUser

# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email', 'password1', 'password2')

# class CustomAuthenticationForm(AuthenticationForm):
#     username_or_email = forms.CharField(label='Username or Email')

class CallCenter_managerSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ('username','email',  'password1', 'password2')
    @transaction.atomic
    def save(self, commit=True):
        user = super(CallCenter_managerSignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_CallCenter_manager = True
        user.save()
        callCenter_manager = CallCenter_manager.objects.create(user=user)
        
        callCenter_manager.save()
 
        return user 
 

class CustomerSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')
    @transaction.atomic
    def save(self, commit=True):
        user = super(CustomerSignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_customer = True
        user.save()
        customer = Customer.objects.create(user=user)
 
        customer.save()
        return user





# class CustomerSignUpForm(UserCreationForm):
#     # first_name = forms.CharField(required=True)
#     # last_name = forms.CharField(required=True)
#     # phone_number = forms.CharField(required=True)
#     # location = forms.CharField(required=True)

#     class Meta(UserCreationForm.Meta):
#         model = CustomUser
 
#     @transaction.atomic
#     def save(self):
#         user = super().save(commit=False)
#         user.is_customer = True
#         # user.first_name = self.cleaned_data.get('first_name')
#         # user.last_name = self.cleaned_data.get('last_name')
#         user.save()
#         customer = Customer.objects.create(user=user)
#         user.save()
#         # customer.phone_number=self.cleaned_data.get('phone_number')
#         # customer.location=self.cleaned_data.get('location')
#         customer.save()
#         return user


class EmployeeSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ('username','email',  'password1', 'password2')
    @transaction.atomic
    def save(self, commit=True):
        user = super(EmployeeSignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_employee = True
        user.save()
        customer = Employee.objects.create(user=user)
 
        customer.save()
        return user
 
 




class ManagerSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ('username','email',  'password1', 'password2')
    @transaction.atomic
    def save(self, commit=True):
        user = super(ManagerSignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_manager = True
        user.save()
        
        manager = Manager.objects.create(user=user)
        
        manager.save()
        return user
 
 
class AdminSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ('username','email',  'password1', 'password2')
    @transaction.atomic
    def save(self, commit=True):
        user = super(AdminSignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_admin = True
        user.save()
        
        admin = Admin.objects.create(user=user)
        
        admin.save()
        return user
   
class MarketingSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ('username','email',  'password1', 'password2')
    @transaction.atomic
    def save(self, commit=True):
        user = super(MarketingSignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_marketing = True
        user.save()
        marketing = Marketing.objects.create(user=user)
        
        marketing.save()
        return user
    
    
class CallCenterSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ('username','email',  'password1', 'password2')
    @transaction.atomic
    def save(self, commit=True):
        user = super(CallCenterSignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_CallCenter = True
        user.save()
        
        callCenter = CallCenter.objects.create(user=user)
        
        callCenter.save()
 
        return user 
       

    
class PatientSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ('username','email',  'password1', 'password2')
    @transaction.atomic
    def save(self, commit=True):
        user = super(PatientSignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_patient = True
        user.save()
        patient= Patient.objects.create(user=user)
        
        patient.save()
 
        return user
    
    
class DoctorSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ('username','email',  'password1', 'password2')
    @transaction.atomic
    def save(self, commit=True):
        user = super(DoctorSignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_doctor= True
        user.save()
        doctor= Doctor.objects.create(user=user)
        
        doctor.save()
 
 
        return user        
 
     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
# class CustomerSignUpForm(UserCreationForm):
 
  
#     class Meta(UserCreationForm.Meta):
#         model = CustomUser
 
#     @transaction.atomic
#     def save(self):
#         user = super().save(commit=False)
        
#         user.is_customer = True
#         user.save()
#         customer= Customer.objects.create(user=user)
        
#         customer.save()
 
#         return customer








# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None):
#         if not email:
#             raise ValueError('Users must have an email address')

#         user = self.model(
#             email=self.normalize_email(email),
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password):
#         user = self.create_user(
#             email=self.normalize_email(email),
#             password=password,
#         )
#         user.is_admin = True
#         user.save(using=self._db)
#         return user

# class CustomUser(AbstractBaseUser):
#     email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
#     username = models.CharField(max_length=30)
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']

#     def __str__(self):
#         return self.email

#     def has_perm(self, perm, obj=None):
#         return True

#     def has_module_perms(self, app_label):
#         return True

#     @property
#     def is_staff(self):
#         return self.is_admin

 



 