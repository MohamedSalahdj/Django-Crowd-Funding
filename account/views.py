from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate
from .forms import SignUpForm, SignUpForm2, UserForm
from django.contrib.auth.models import User
from .models import Profile
from campaign.models import Project, ProjectImage, Category, Donate
from django.contrib.auth.decorators import login_required


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
    else:
        form = SignUpForm()
        form2 = SignUpForm2()
    return render(request, 'registration/signup.html', {'form': form, 'form2': form2})


@login_required
def show_profile(request):
    user = Profile.objects.get(user=request.user)

    context = {
        'user':user
        }
    return render(request, 'registration/user_profile.html', context)

@login_required
def edit_profile(request):
    user_profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = SignUpForm2(request.POST, request.FILES, instance=user_profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form = user_form.save()
            profile_form = profile_form.save(commit=False)
            profile_form.user = request.user
            profile_form.save()
    else:
        user_form = UserForm(instance=request.user)
        profile_form = SignUpForm2(instance=user_profile)

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
    pass

@login_required
def delete_profile(request):
    user = User.objects.get(username=request.user)
    profile = Profile.objects.get(user=user)
    profile.delete()
    user.delete()
    return redirect('/')