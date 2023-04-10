   
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

#  AbstractUser for authenticated
class User(AbstractUser):
 
    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'admin'
        EMPLOYEE = "EMPLOYEE", "employee"
        # DELIVERY = "DELIVERY", "delivery"
        MANAGER = "MANAGER", "manager"
        CUSTOMER = "CUSTOMER", "customer"
        CALLCENTER = "CALLCENTER", "callCenter"    
        MARKETING = "MARKETING", "marketing"
        DOCTOR = "DOCTOR", "doctor"
        PATIENT = "PATIENT", "patient"
        CALLCENTERMANAGER = "CALLCENTERMANAGER", "callcentermanager"   
        
        
    role = models.CharField(max_length=50, help_text='This is role user in system', choices=Role.choices)
    email = models.EmailField(unique=True)
    # username = models.EmailField(unique=True)

    set_role = Role.ADMIN
    # avatar = models.ImageField(null=True, default="avatar.svg")
    # USERNAME_FIELD = 'username'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    def is_admin(self):
        return self.role == self.Role.ADMIN

    def is_employee(self):
        return self.role == self.Role.EMPLOYEE

    # def is_delivery_company(self):
    #     return self.role == self.Role.DELIVERY

    def is_manager(self):
        return self.role == self.Role.MANAGER

    def is_customer(self):
        return self.role == self.Role.CUSTOMER

    def is_callcentermanager(self):
        return self.role == self.Role.CALLCENTERMANAGER

    def is_callCenter(self):
        return self.role == self.Role.CALLCENTER

    def is_marketing(self):
        return self.role == self.Role.MARKETING

    def is_doctor(self):
        return self.role == self.Role.DOCTOR
    
    def is_patient(self):
        return self.role == self.Role.PATIENT


    def save(self, *args, **kwargs):
        if not self.pk:
            if not self.role == User.Role.ADMIN:
                self.role = self.set_role
            return super().save(*args, **kwargs)
        return super().save(*args, **kwargs)




class EmployeeManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role="EMPLOYEE")


class Employee(User):
    set_role = User.Role.EMPLOYEE
    employees = EmployeeManager()

    class Meta:
        proxy = True



# class DeliveryManager(models.Manager):
#     def get_queryset(self, *args, **kwargs):
#         results = super().get_queryset(*args, **kwargs)
#         return results.filter(role="DELIVERY")


# class Delivery(User):
#     set_role = User.Role.DELIVERY
#     REQUIRED_FIELDS = ['username']
#     companies = DeliveryManager()

#     class Meta:
#         proxy = True
    

class managerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role="MANAGER")


class Manager(User):
    set_role = User.Role.MANAGER
    REQUIRED_FIELDS = ['username']
    companies = managerManager()

    class Meta:
        proxy = True
    
    
    
class CustomerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role="CUSTOMER")


class Customer(User):
    set_role = User.Role.CUSTOMER
    REQUIRED_FIELDS = ['username']
    companies = CustomerManager()

    class Meta:
        proxy = True

        
class CallCenterManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role="CALLCENTER")


class CallCenter(User):
    set_role = User.Role.CALLCENTER
    REQUIRED_FIELDS = ['username']
    companies = CallCenterManager()

    class Meta:
        proxy = True
  
class MarketingManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role="MARKETING")


class Marketing(User):
    set_role = User.Role.MARKETING
    REQUIRED_FIELDS = ['username']
    companies = MarketingManager()

    class Meta:
        proxy = True

class DoctorManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role="DOCTOR")


class Doctor(User):
    set_role = User.Role.DOCTOR
    REQUIRED_FIELDS = ['username']
    companies = DoctorManager()

    class Meta:
        proxy = True
  
class PatientManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role="PATIENT")


class Patient(User):
    set_role = User.Role.PATIENT
    REQUIRED_FIELDS = ['username']
    companies = PatientManager()

    class Meta:
        proxy = True    
        
class CallcentermanagerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role="CALLCENTERMANAGER")


class Callcentermanager(User):
    set_role = User.Role.CALLCENTERMANAGER
    REQUIRED_FIELDS = ['username']
    companies = CallcentermanagerManager()

    class Meta:
        proxy = True    
        
      