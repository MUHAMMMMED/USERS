from django.shortcuts import redirect, render
from .forms import SignupForm , UserForm , ProfileForm
from django.contrib.auth import authenticate, login
from .models import Profile
from django.urls import reverse


# Create your views here.


def signup(request):
    if request.method=="POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('profile/')
    else:
        form = SignupForm()
    return render(request,'registration/signup.html',{'form':form})




def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request,'accounts/profile.html',{'profile': profile})



def profile_edit(request):
    profile = Profile.objects.get(user=request.user)

    if request.method=='POST':
        userform = UserForm(request.POST,instance=request.user)
        profileform = ProfileForm(request.POST,request.FILES,instance=profile )
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse('accounts:profile'))

    else :
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)

    return render(request,'accounts/profile_edit.html',{'userform':userform , 'profileform':profileform})



# def password_reset_request(request):
# 	if request.method == "POST":
# 		password_reset_form = PasswordResetForm(request.POST)
# 		if password_reset_form.is_valid():
# 			data = password_reset_form.cleaned_data['email']
# 			associated_users = User.objects.filter(Q(email=data))
# 			if associated_users.exists():
# 				for user in associated_users:
# 					subject = "Password Reset Requested"
# 					email_template_name = "main/password/password_reset_email.txt"
# 					c = {
# 					"email":user.email,
# 					'domain':'127.0.0.1:8000',
# 					'site_name': 'Website',
# 					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
# 					'token': default_token_generator.make_token(user),
# 					'protocol': 'http',
# 					}
# 					email = render_to_string(email_template_name, c)
# 					try:
# 						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
# 					except BadHeaderError:

# 						return HttpResponse('Invalid header found.')
						
# 					messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
# 					return redirect ("main:homepage")
# 	password_reset_form = PasswordResetForm()
# 	return render(request=request, template_name="main/password/password_reset.html", context={"password_reset_form":password_reset_form})
# from django.shortcuts import render,redirect
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
# from django.contrib import messages
# from .models import *
# from django.contrib.auth import authenticate,login,logout
# from .helpers import send_forget_password_mail


# def ChangePassword(request , token):
#     context = {}
    
    
#     try:
#         profile_obj = Profile.objects.filter(forget_password_token = token).first()
#         context = {'user_id' : profile_obj.user.id}
        
#         if request.method == 'POST':
#             new_password = request.POST.get('new_password')
#             confirm_password = request.POST.get('reconfirm_password')
#             user_id = request.POST.get('user_id')
            
#             if user_id is  None:
#                 messages.success(request, 'No user id found.')
#                 return redirect(f'/change-password/{token}/')
                
            
#             if  new_password != confirm_password:
#                 messages.success(request, 'both should  be equal.')
#                 return redirect(f'/change-password/{token}/')
                         
            
#             user_obj = User.objects.get(id = user_id)
#             user_obj.set_password(new_password)
#             user_obj.save()
#             return redirect('/login/')
            
            
            
        
        
#     except Exception as e:
#         print(e)
#     return render(request , 'change-password.html' , context)


# import uuid
# def ForgetPassword(request):
#     try:
#         if request.method == 'POST':
#             username = request.POST.get('username')
            
#             if not User.objects.filter(username=username).first():
#                 messages.success(request, 'Not user found with this username.')
#                 return redirect('/forget-password/')
            
#             user_obj = User.objects.get(username = username)
#             token = str(uuid.uuid4())
#             profile_obj= Profile.objects.get(user = user_obj)
#             profile_obj.forget_password_token = token
#             profile_obj.save()
#             send_forget_password_mail(user_obj.email , token)
#             messages.success(request, 'An email is sent.')
#             return redirect('/forget-password/')
                
    
    
#     except Exception as e:
#         print(e)
#     return render(request , 'forget-password.html')