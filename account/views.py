from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate
from .forms import SignUpForm, SignUpForm2, UserForm, ProfileForm
from django.contrib.auth.models import User
from .models import Profile
from campaign.models import Project, ProjectImage, Category, Donate
from django.contrib.auth.decorators import login_required
import time

from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from project import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import authenticate, login, logout
from . tokens import generate_token


def signup(request):
    form = SignUpForm()
    form2 = SignUpForm2()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        form2 = SignUpForm2(request.POST, request.FILES)

        if form.is_valid() and form2.is_valid():
            user = form.save()
            profile = form2.save(commit=False)
            profile.user = user
            profile.save()
            # Email Address Confirmation Email         
               
            # Welcome Email
            subject = "Welcome to Kind Heart Charity Login!!"
            #message = "Hello " + user.first_name + "!! \n" + "Welcome to Kind Heart Charity !! \nThank you for visiting our website\n. We have also sent you a confirmation email, please confirm your email address. \n\nThanking You\nShovit Nepal"                
            message = render_to_string('registration/welcome_email_message.html',{                
                'name': user.first_name,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': generate_token.make_token(user)
            })
            email = EmailMessage(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
            )            
            email.content_subtype = 'html'
            email.send() 
            #send_mail(subject, message, from_email, to_list, fail_silently=True)     
               
            # Email Address Confirmation Email
            current_site = get_current_site(request)
            email_subject = "Confirm your Email @ Kind Heart Charity!!"
            message2 = render_to_string('registration/email_confirmation.html',{                
                'name': user.first_name,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': generate_token.make_token(user)
            })
            email = EmailMessage(
                email_subject,
                message2,
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
            )            
            email.content_subtype = 'html'
            email.send() 
            return redirect('verify_email')
        
    else:
        form = SignUpForm()
        form2 = SignUpForm2()
    return render(request, 'registration/signup.html', {'form': form, 'form2': form2})
    
def verify_email(request):     
    context=messages.success(request, "Your Account has been created succesfully!!")           
    return render(request, 'registration/verify_email.html', context)


def activate(request,uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser, token):
        print('what is hereeeeeeeeeeeee    ',myuser)
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()
        login(request, myuser)
        return redirect('login')
    else:
        return render(request,'registration/activation_failed.html')
    
@login_required
def show_profile(request):
    user = Profile.objects.get(user=request.user)
    if request.method == 'GET':
        context = {
            'user':user
            }
        return render(request, 'registration/user_profile.html', context)
    else:
        input_pass = request.POST.get('user_password')
        user_info = User.objects.get(username=request.user)
        if(user_info.check_password(input_pass)):
            profile = Profile.objects.get(user=user_info)
            profile.delete()
            user_info.delete()
            return redirect('/')
        else:
            context = {"user": user, 
                        "error_msg": "Incorrect Password"}
            return render(request, 'registration/user_profile.html', context=context)
            

@login_required
def edit_profile(request):
    user_profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form = user_form.save()
            profile_form = profile_form.save(commit=False)
            profile_form.user = request.user
            profile_form.save()
            messages.success(request, 'edit successfully ')

            return redirect('edit_profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=user_profile)

    context = {
        'user_form' : user_form,
        'profile_form' : profile_form
    }
    return render(request, 'registration/edit_profile.html', context)        

@login_required
def user_projects(request):
    projects = Project.objects.filter(owner=request.user)

    context = {
        'projects': projects
    }

    return render(request, 'user-activity/user_project.html', context)

@login_required
def user_donations(request):
    user_donations = Donate.objects.filter(donator=request.user)
    
    context = {
        'user_donations' : user_donations
    }

    return render(request, 'user-activity/user_donations.html', context)


