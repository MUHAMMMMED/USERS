from django.db import models
from django.utils import timezone
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import User
# from django.contrib.auth.signals import user_logged_in
# from django.utils import  timezone
 
   
   

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
   
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError('Users must have a username')
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

# class CustomUserManager(BaseUserManager):
#        def create_user(self, email, password=None, **extra_fields):
#            if not email:
#                raise ValueError('The Email field must be set')
#            email = self.normalize_email(email)
#            user = self.model(email=email, **extra_fields)
#            user.set_password(password)
#            user.save(using=self._db)
#            return user

#        def create_superuser(self, email, password=None, **extra_fields):
#            extra_fields.setdefault('is_staff', True)
#            extra_fields.setdefault('is_superuser', True)

#            if extra_fields.get('is_staff') is not True:
#                raise ValueError('Superuser must have is_staff=True.')
#            if extra_fields.get('is_superuser') is not True:
#                raise ValueError('Superuser must have is_superuser=True.')

#            return self.create_user(email, password=password, **extra_fields)
   


class CustomUser(AbstractBaseUser):
       username = models.CharField(max_length=30, unique=True)
       email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    #    first_name = models.CharField(max_length=30)
    #    last_name = models.CharField(max_length=30)
       is_active = models.BooleanField(default=True)
       is_admin = models.BooleanField(default=False)
       is_manager= models.BooleanField(default=False)
       is_CallCenter_manager= models.BooleanField(default=False)
       is_marketing= models.BooleanField(default=False)
       is_CallCenter= models.BooleanField(default=False)
       is_patient = models.BooleanField(default=False)
       is_doctor = models.BooleanField(default=False)
       is_customer= models.BooleanField(default=False)
       is_employee = models.BooleanField(default=False)
       phone_number = models.CharField(max_length=20)
       date_joined = models.DateTimeField(verbose_name='date_joined', auto_now_add=True)
       last_login = models.DateTimeField(verbose_name='last_login', auto_now=True)   




    #    USERNAME_FIELD = 'email'
    #    REQUIRED_FIELDS = ['first_name', 'last_name']

    #    objects = CustomUserManager()

    #    def __str__(self):
    #        return self.email

    #    def has_perm(self, perm, obj=None):
    #        return True

    #    def has_module_perms(self, app_label):
    #        return True
       objects = CustomUserManager()

       USERNAME_FIELD = 'username'
       REQUIRED_FIELDS = ['email']
       def __str__(self):
          return self.username

       def has_perm(self, perm, obj=None):
         return True

       def has_module_perms(self, app_label):
          return True

       @property
       def is_staff(self):
           return self.is_admin
   
   
    
   
class Admin(models.Model):
    
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,primary_key=True)
    #  avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    def __str__(self):
         return self.user.username  
 
 

class Employee(models.Model):
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE, primary_key = True)
    def __str__(self):
         return self.user.username  
    
    
class Manager(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,primary_key=True)
    def __str__(self):
         return self.user.username   
    
class Customer(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,primary_key=True)
    def __str__(self):
         return self.user.username  
    
class CallCenter(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,primary_key=True)
    def __str__(self):
         return self.user.username  
    
    
class Marketing(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,primary_key=True)
    def __str__(self):
         return self.user.username  
    
class Doctor(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,primary_key=True)
    def __str__(self):
         return self.user.username  
class Patient(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,primary_key=True)
    def __str__(self):
         return self.user.username  
    
class CallCenter_manager(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,primary_key=True)
    def __str__(self):
         return self.user.username  
   

   
   
   
   
   
   
   
   
   
   
   
   
   
# from datetime import date
# from django.db import models
# from django.contrib.auth.models import PermissionsMixin, AbstractUser
# from django.contrib.auth.base_user import AbstractBaseUser
# from django.utils.translation import ugettext_lazy as _
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# from allauth.socialaccount.models import SocialAccount
# from .manager import UserManager


# class User(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(_('username'), max_length=130, unique=True)
#     full_name = models.CharField(_('full name'), max_length=130, blank=True)
#     email = models.EmailField(_('email id'), max_length=50, blank=True)
#     is_staff = models.BooleanField(_('is_staff'), default=False)
#     is_active = models.BooleanField(_('is_active'), default=True)
#     date_joined = models.DateField(_("date_joined"), default=date.today)
#     phone_number_verified = models.BooleanField(default=False)
#     change_pw = models.BooleanField(default=True)
#     phone_number = models.BigIntegerField(blank=True, null=True)
#     country_code = models.IntegerField(blank=True, null=True)
#     profile_picture = models.URLField(blank=True, null=True)

#     objects = UserManager()

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['full_name',]

#     class Meta:
#         ordering = ('username',)
#         verbose_name = _('user')
#         verbose_name_plural = _('users')

#     def get_short_name(self):
#         return self.username


# def save_profile(sender, instance, **kwargs):
#     print(instance)
#     instance.user.full_name = instance.extra_data['name']
#     uid = instance.extra_data['id']
#     instance.user.profile_picture = instance.get_avatar_url()
#     instance.user.save()

# post_save.connect(save_profile, sender=SocialAccount)
    
# class Pat(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
#     name = models.CharField(max_length=100)       
#     image = models.ImageField(default='default.jpg', upload_to='Patient_pics')


#     def __str__(self):
#         return '{} Patient.'.format(self.user.username)

#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)

#         img = Image.open(self.image.path)
#         if img.width > 300 or img.height > 300:
#             output_size = (300, 300)
#             img.thumbnail(output_size)
#             img.save(self.image.path)


# def create_profile_Patient(sender, **kwarg):
#     if kwarg['created']:
#         Profile.objects.create(user=kwarg['instance'])


# post_save.connect(create_profile_Patient, sender=User)    
    
    
            
# class CallCenterProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     CallCenter_id = models.IntegerField(null=True, blank=True)
    
# class TeacherProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     teacher_id = models.IntegerField(null=True, blank=True)


# @receiver(post_save, sender=Teacher)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created and instance.role == "TEACHER":
#         CallCenterProfile.objects.create(user=instance)
    
    
# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# class Account(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(verbose_name="email", max_length=60, unique=True)
#     name = models.CharField(max_length=30)
#     date_joined = models.DateTimeField(verbose_name='date_joined', auto_now_add=True)
#     last_login = models.DateTimeField(verbose_name='last_login', auto_now=True)
#     is_admin = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['name']
#     objects = MyAccountManager()

#     def __str__(self):
#         return self.email
    
    
    
    
    
    
    
    
    
    
    
    

    
# class User(AbstractUser):
#     is_student = models.BooleanField('student status', default=False)
#     is_teacher = models.BooleanField('teacher status', default=False)
    
    
# class User(AbstractUser):
#   USER_TYPE_CHOICES = (
#       (1, 'student'),
#       (2, 'teacher'),
#       (3, 'secretary'),
#       (4, 'supervisor'),
#       (5, 'admin'),
#   )

#   user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)

# class Role(models.Model):
#   '''
#   The Role entries are managed by the system,
#   automatically created via a Django data migration.
#   '''
#   STUDENT = 1
#   TEACHER = 2
#   SECRETARY = 3
#   SUPERVISOR = 4
#   ADMIN = 5
#   ROLE_CHOICES = (
#       (STUDENT, 'student'),
#       (TEACHER, 'teacher'),
#       (SECRETARY, 'secretary'),
#       (SUPERVISOR, 'supervisor'),
#       (ADMIN, 'admin'),
#   )

#   id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

#   def __str__(self):
#       return self.get_id_display()


# class User(AbstractUser):
#   roles = models.ManyToManyField(Role)




