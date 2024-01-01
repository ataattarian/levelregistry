from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from django.utils.html import format_html

# Register your models here.

class UserAdmin(BaseUserAdmin):
    list_display = ['email', 'first_name', 'last_name', 'is_active', 'is_staff']
    search_fields = ['email', 'first_name', 'last_name']
    list_filter = ['is_active', 'is_staff']
    fieldsets = (None,{
        'fields':('email','phoneNumber','birthdate','city','state','grade','school_name')
    })
    
admin.site.register(User, UserAdmin)