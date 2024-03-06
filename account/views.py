from django.shortcuts import render
from django.contrib.auth import login,authenticate
from .forms import SignUpForm,SignUpForm2


# Create your views here.

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


