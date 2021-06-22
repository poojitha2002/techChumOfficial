from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


CLG_CHOICES= [
    ('IIT', 'IIT'),
    ('NIT', 'NIT'),
    ('BITs', 'BITs'),
    ('VIT', 'VIT'),
    ('RVCE','RVCE'),
    ('KLEF','KLEF'),
    ('Other','Other')
    ]
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    clg = forms.CharField(label='College / University : ', widget=forms.Select(choices=CLG_CHOICES))


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','clg']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
