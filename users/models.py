from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email,username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)
    
class User(AbstractUser):
    email = models.EmailField(unique=True)
    phoneNumber = models.CharField(max_length=15, null=True, blank=True)
    birthdate = models.CharField(max_length=10,null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    grade = models.CharField(max_length=10, null=True, blank=True)
    school_name = models.CharField(max_length=100, null=True, blank=True)
    signature = models.ImageField(upload_to ='signature/',null=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    objects = UserManager()

    
    def __str__(self):
        return self.email