from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=15)
    last_name = forms.CharField(max_length=15)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError('Username already exists')
        return username

    def clean_email(self):
        email_value = self.cleaned_data['email']

        
        if User.objects.filter(email=email_value).exists():
            raise forms.ValidationError('This email already exists')

        return email_value    
        

class SignUpForm2(forms.ModelForm):
    phone = forms.CharField(
        label="Mobile phone",
        
        max_length=12,
        validators=[RegexValidator(
            regex='^01[0|1|2|5][0-9]{8}$',
            message='Phone must start with 010, 011, 012, 015, and contain 11 digits',
            
        )]
    )
    image = forms.ImageField(label="Profile Picture")

    # birth_date = forms.DateField(required=False)
    # facebook_profile = forms.URLField(required=False)
    # country = forms.CharField(max_length=2)
    class Meta:
        model = Profile
        fields = ['phone', 'image']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class ProfileForm(forms.ModelForm):
    birth_date = forms.DateField(required=False)
    facebook_profile = forms.URLField(required=False)
    country = forms.CharField(max_length=2)
    class Meta:
        model = Profile
        fields = ['phone', 'image', 'birth_date', 'facebook_profile', 'country']