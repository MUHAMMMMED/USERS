from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from test.models  import *
from phonenumber_field.formfields import PhoneNumberField
# "admin.py"
from phonenumber_field.widgets import PhoneNumberPrefixWidget

#      class Meta:
#              widgets = {'PhoneNumber': PhoneNumberPrefixWidget(initial='SA'),
            
#         }
 
# "settings.py"

# PHONENUMBER_DEFAULT_REGION = "US"

# PHONENUMBER_DB_FORMAT = 'NATIONAL'
# PHONENUMBER_DEFAULT_REGION = "SA"`
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget



 
# from django.conf import settings
# from django.core import validators
# from django.core.exceptions import ValidationError
# from django.forms.fields import CharField


# from phonenumber_field.phonenumber import to_python, validate_region
# from phonenumber_field.validators import validate_international_phonenumber
# from phonenumber_field.widgets import RegionalPhoneNumberWidget






# from django import forms
# from phonenumber_field.formfields import PhoneNumberField
# from phonenumber_field.widgets import USPhoneNumberMultiWidget

# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=255)
#     phone_number = PhoneNumberField(widget=USPhoneNumberMultiWidget(attrs={'class': 'custom-input'}))
#     message = forms.CharField(widget=forms.Textarea)




class OfersBookingform(forms.ModelForm):
    # Phonenumber = PhoneNumberField(widget=PhoneNumberPrefixWidget(initial='IN'))
    phone_number = PhoneNumberField(
        region="SA",

        # widget=PhoneNumberPrefixWidget(
        #     initial="SA",
        #     country_choices=[
        #          ("SA", "SAUDI ARABIA"),
        #     #      ("FR", "France"),
        #     ],
        # ),
     
    ) 




    Message = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = OffersBooking
 
        fields = "__all__"

        # widgets = {                          # Here
        #     'PhoneNumber': PhoneNumberPrefixWidget(initial='US'),
        # }



        exclude = ['patients','offer','date' ]   
    #      = PhoneNumberField(widget=PhoneNumberPrefixWidget(initial='SA'))
    # PhoneNumber = PhoneNumberField(
    #     widget=PhoneNumberPrefixWidget(attrs={'class': 'form-control'})
    # )
 
    # …
    # PhoneNumber = PhoneNumberField(widget=PhoneNumberPrefixWidget(initial='GE'))
    # PhoneNumber.error_messages['invalid'] = 'Incorrect International Calling Code or Mobile Number!'



    # def clean_phone(self):
    #     PhoneNumber = self.cleaned_data.get("PhoneNumber")
    #     z = PhoneNumberField.parse(PhoneNumber, "IN")
    #     if not PhoneNumberField.is_valid_number(z):
    #         raise forms.validationError("Number not in SG format")
    #     return PhoneNumber
   

class Ofersform(forms.ModelForm):
    class Meta:
        model = Offers
 
        fields = "__all__"

class PATIENTform(forms.ModelForm):
    phone_number = PhoneNumberField(
        region="SA",

        # widget=PhoneNumberPrefixWidget(
        #     initial="SA",
        #     country_choices=[
        #          ("SA", "SAUDI ARABIA"),
        #     #      ("FR", "France"),
        #     ],
        # ),
     
    ) 
    class Meta:
        model = PATIENT
 
        fields = "__all__"



















#         from django import forms

# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=30)
#     email = forms.EmailField(max_length=254)
#     message = forms.CharField(
#         max_length=2000,
#         widget=forms.Textarea(),
#         help_text='Write here your message!'
#     )
#     source = forms.CharField(       # A hidden input for internal use
#         max_length=50,              # tell from which page the user sent the message
#         widget=forms.HiddenInput()
#     )

#     def clean(self):
#         cleaned_data = super(ContactForm, self).clean()
#         name = cleaned_data.get('name')
#         email = cleaned_data.get('email')
#         message = cleaned_data.get('message')
#         if not name and not email and not message:
#             raise forms.ValidationError('You have to write something!')