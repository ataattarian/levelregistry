from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import User
from .forms import RegisterForm
import base64
from django.core.files.base import ContentFile
# Create your views here.


class UserRegistrationView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('success')

def final(request):
    return render(request=request,template_name='final.html')