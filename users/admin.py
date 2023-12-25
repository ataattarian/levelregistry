from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from django.utils.html import format_html

# Register your models here.

class UserAdmin(BaseUserAdmin):
    list_display = ['email', 'first_name', 'last_name', 'is_active', 'is_staff','display_signature']
    search_fields = ['email', 'first_name', 'last_name']
    list_filter = ['is_active', 'is_staff']
    
    def display_signature(self, obj):
        if obj.signature:
            return format_html('<img src="{}" width="50" height="50" />', obj.signature.url)
        return None
    display_signature.short_description = 'Signature'
    
admin.site.register(User, UserAdmin)