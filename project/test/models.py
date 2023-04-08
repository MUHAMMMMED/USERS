from django.db import models
from phonenumber_field.phonenumber import PhoneNumber
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from phone_field import PhoneField
from django.core.validators import RegexValidator
from Accounts.models import *

class PATIENT(models.Model):
    date_joined =models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=300,blank=True, null=True)  
    city= models.CharField(max_length=300,blank=True, null=True)
    phone_number = PhoneNumberField( unique = True  )
    def __str__(self):
        return self.name

 
class Offers(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    servesname = models.CharField(max_length=100)
    price= models.CharField(max_length=300)
    descrption= models.CharField(max_length=300)
 
    class Meta:
      ordering = ("-created_at",)

    def __str__(self):
        return self.servesname



class Property(models.Model):
     title = models.CharField(max_length=100)
     date = models.DateField(null=True)  
     def __str__(self):
      return self.title
 
 
 
 
class Doctor(Property):
     pass
 

class Knew(Property):
     pass

 
class Section(Property):
     pass
 
 
 
 
class OffersBooking(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    Callcenter = models.ForeignKey(CallCenter, on_delete=models.CASCADE,blank=True, null=True)
    offer = models.ForeignKey(Offers, on_delete=models.SET_NULL,blank=True, null=True)
    section= models.ForeignKey(Section,on_delete=models.CASCADE ,null=True)
    doctor= models.ForeignKey(Doctor,on_delete=models.CASCADE ,null=True)
    knew= models.ForeignKey(Knew,on_delete=models.CASCADE ,null=True)
    patients = models.ForeignKey(PATIENT, related_name='pATIENT', on_delete=models.CASCADE,blank=True, null=True)
    name = models.CharField(max_length=100,blank=True, null=True)
    Message= models.CharField(max_length=300,blank=True, null=True)
    phone_number = PhoneNumberField()
    date = models.DateField(null=True)  
 
    class Meta:
      ordering = ("-created_at",)

    def __str__(self):
        return self.name


    # phone = PhoneNumberField(blank=True,help_text="plase enter your phone number",max_length=16)
  