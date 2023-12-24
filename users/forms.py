from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegistrationForm(UserCreationForm):
    phoneNumber = forms.CharField(max_length=15, required=True)
    birthdate = forms.DateField(required=True)
    city = forms.ChoiceField(choices=[('tehran', 'Tehran'), ('isfahan', 'Isfahan')], required=True)
    state = forms.ChoiceField(choices=[('tehran', 'Tehran'), ('esfahan', 'Esfahan')], required=True)
    grade = forms.CharField(max_length=10, required=True)
    school_name = forms.CharField(max_length=100, required=True)
    
    class Meta:
        model = User
        fields = ['email', 'phoneNumber', 'birthdate', 'city', 'state', 'grade', 'school_name']