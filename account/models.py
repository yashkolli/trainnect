from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self,email,first_name,year,rollno,branch,password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not first_name:
            raise ValueError("Users must have a first_name")
        if not year:
            raise ValueError("Users must mention their year")
        if not rollno:
            raise ValueError("Users must have a roll number")
        if not branch:
            raise ValueError("Users must have a branch")

        user=self.model(
                email=self.normalize_email(email),
                first_name=first_name,
                year=year,
                rollno=rollno,
                branch=branch,
            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,first_name,year,rollno,branch,password):
        user=self.create_user(
                email=self.normalize_email(email),
                password=password,
                first_name=first_name,
                year=year,
                rollno=rollno,
                branch=branch,
            )
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email= models.EmailField(verbose_name="email",max_length=60,unique=True)
    date_joined=models.DateTimeField(verbose_name="date joined",auto_now_add=True)
    last_login=models.DateTimeField(verbose_name="last login",auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100, blank = True)
    mobile_regex=RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    mobileno=models.CharField(validators=[mobile_regex], max_length=17, blank = True)
    rollno=models.CharField(unique=True,max_length=15)
    branch=models.CharField(max_length=100)
    year=models.CharField(max_length=10)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','year','rollno','branch']

    objects=MyAccountManager()

    def __str__(self):
        return self.first_name

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True



