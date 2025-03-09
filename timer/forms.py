from django import forms
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Timer

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True) 
    last_name = forms.CharField(max_length=50, required=True) 
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'password1', 'password2']

class CreateTimer(forms.ModelForm):
    title = forms.CharField(max_length=50, required=True) 
    hours = forms.IntegerField(min_value=0, required=True) 
    minutes = forms.IntegerField(min_value=0, max_value=59, required=True) 
    seconds = forms.IntegerField(min_value=0, max_value=59, required=True)
    owner = forms.IntegerField(widget = forms.HiddenInput())
    
    class Meta:
        model = Timer
        fields = ['title', 'hours', 'minutes', 'seconds', 'owner']