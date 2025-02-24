from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager , PermissionsMixin


class UsersManager(BaseUserManager):
    def create_user(self, email , password=None , **extra_fields):    
        if not email:
            raise ValueError("Please enter email address")

        email  = self.normalize_email(email) # normalize is to verfiy if the email is in valid format 
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password=None ,**extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", False)
        return self.create_user(email,password,**extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=200 , blank = True) 
    last_name = models.CharField(max_length=200 , blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined  = models.DateTimeField(auto_now_add=True)
    
    objects = UsersManager()
    
    USERNAME_FIELD = 'email'
    
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        return self.email

    


