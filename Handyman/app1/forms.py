
from django.contrib.auth.forms import UserCreationForm
from .models import Client, MaintenanceTechnician

from django import forms
from django.contrib.auth.models import User
from .models import Client, MaintenanceTechnician

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
class ClientSignUpForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('address', 'phone_number')

class TechnicianSignUpForm(forms.ModelForm):
    class Meta:
        model = MaintenanceTechnician
        fields = ('specialization', 'experience_years')