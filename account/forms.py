from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=15)
    last_name = forms.CharField(max_length=15)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'username', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError('Username already exists')
        return username
        

class SignUpForm2(forms.ModelForm):
    phone = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"placeholder": "phone"}),
        max_length=12,
        validators=[RegexValidator(
            regex='^01[0|1|2|5][0-9]{8}$',
            message='Phone must be start 010, 011, 012, 015 and all number contains 11 digits',
            code='invalid number'
        )]
    )
    image = forms.ImageField(label="")

    class Meta:
        model = Profile
        fields = ['phone', 'image']


