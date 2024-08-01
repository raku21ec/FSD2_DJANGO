from django import forms
from .models import BusTicket

class BusTicketForm(forms.ModelForm):
    class Meta:
        model = BusTicket
        fields = ['passenger_name', 'email', 'departure_city', 'destination_city', 'departure_time', 'seat_number']

#LOGIN/SIGNUP

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(label=("Password"), strip=False, widget=forms.PasswordInput)



