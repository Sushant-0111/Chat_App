from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager , PermissionManager



class UsersManager(BaseUserManager):
    def create_user(self, email , password=None , **extra_fields):    
        if not email:
            raise ValueError("Please enter email address")

        email  = self.normalize_email(email) # normalize is to verfiy if the email is in valid format 
        user = self.model(email = email, **extra_fields)
        user.models.PositiveIntegerField(_(""))
        user.set(password)
        user.save()
        return user
    
    def create_superuser(self, email, password=None ,**extrafields):
        
        


