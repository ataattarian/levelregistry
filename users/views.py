from django.shortcuts import render
from .forms import RegistrationForm
from .models import User
from jdatetime import date as jdate
# Create your views here.


def register(request):
    if request.method == 'POST':
        print(request.POST)

    return render(request, 'register.html')