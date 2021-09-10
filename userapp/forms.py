from django import forms

from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm


class SignupForm(forms.ModelForm):


    class Meta:
        first_name = forms.CharField(label="Name", widget=(forms.TextInput(attrs={'class': 'form-control bg-white'}))),
        last_name = forms.CharField(label="Enter Your Last Name", widget=(forms.TextInput(attrs={'class': 'form-control bg-info'}))),
        email = forms.EmailField(label="Enter Your Last Name", widget=(forms.EmailInput(attrs={'class': 'form-control bg-info'}))),
        model=User

        fields=['first_name', 'last_name', 'email', 'username', 'password']
       
       
class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username','password']