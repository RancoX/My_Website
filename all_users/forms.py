from dataclasses import field
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# extend the field of original dj UserCreationForm
class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        # tells the class to save the new form to User
        model=User
        # specifies the order of our extended form password1 is password field and password2 is the confirm pw
        fields=['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username','email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image']