from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import RepairRequest


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(forms.Form):
    username = forms.CharField(max_length = 150)
    password = forms.CharField(widget=forms.PasswordInput)

class RepairRequestForm(forms.ModelForm):
    class Meta:
        model = RepairRequest
        fields = ('device_name', 'description_problem', 'preferred_date_time_repair', 'contact_info')
        widgets = {
            'preferred_date_time_repair': forms.DateTimeInput(attrs={'class': 'datetime-local'}),
        }
