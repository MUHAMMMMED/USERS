from django.contrib import admin
from Accounts.models import *

# # Register your models here.
admin.site.register(CustomUser)
admin.site.register(Manager)
admin.site.register(Customer)
admin.site.register(CallCenter)
admin.site.register(Marketing)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(CallCenter_manager)
admin.site.register(Employee)
admin.site.register(Admin)