from typing import Any
from django import forms
from django.forms import ModelForm
from .models import User
from django.utils import timezone
from django.core.exceptions import ValidationError

class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "birthdate",
            "phoneNumber",
            "email",
            "state",
            "city",
            "school_name",
            "grade",
            "signature"
            ]
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = user.email
        if commit:
            user.save()
        return user
    
    def clean_birthdate(self):
        birthdate = self.cleaned_data.get('birthdate')
        print(self.cleaned_data.get('signature'))
        # Your custom validation logic for the birthdate field
        if birthdate:
            age = 1403 - int(birthdate.split('/')[0])
            if age > 17:
                raise ValidationError(
                    f"این مسابقات برای نوجوانان زیر ۱۷ سال میباشد",
                )

        return birthdate