from django.db import models
from django.contrib.auth.models import AbstractUser , BaseUserManager , PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self , email , password , **extra_fileds):
        if not email:
            raise ValueError("The email must be filled")
        email = self.normalize_email(email)
        user = self.model(email = email , **extra_fileds)
        user.set_password(password)
        user.save(using  = self._db)
        return user


    def create_superuser(self, email , password = None , **extra_fileds):
        extra_fileds.setdefault(is_staff = True)
        extra_fileds.setdefault(is_superuser = True)
        return self.create_user(email , password , **extra_fileds)
    
class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=200 , blank = True)
    last_name = models.CharField(max_length=200 , blank = True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now_add=True)


    objects = UserManager()


    USERNAME_FIELD = 'email'


    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self) -> str: 
        return self.email

