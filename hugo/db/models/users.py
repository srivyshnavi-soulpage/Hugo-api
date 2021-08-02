from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from datetime import datetime
from django.utils import timezone
class UserManager(BaseUserManager):

    use_in_migrations = True
    def _create_user(self, email, password, **extra_fields):

       """
       Creates and saves a User with the given email and password.

       """

       if not email:
           raise ValueError("The given email must be set")

       email = self.normalize_email(email)
       user = self.model(email=email, **extra_fields)
       user.set_password(password)
       user.save(using=self._db)
       return user

    def create_user(self, email, password=None, **extra_fields):
       extra_fields.setdefault("is_superuser", False)
       return self._create_user(email, password, **extra_fields)
    def create_superuser(self, email, password, **extra_fields):
       extra_fields.setdefault("is_superuser", True)
       extra_fields.setdefault("is_staff", True)
       if extra_fields.get("is_superuser") is not True:
           raise ValueError("Superuser must have is_superuser=True.")
       return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True, null=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_field_operator = models.BooleanField(default=False)
    is_qc = models.BooleanField(default=False)
    token = models.CharField(max_length=256, null=True, blank=True)
    token_status = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        db_table = "Users"

    def __str__(self):

        email = self.email
        return email

class Salary(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    bankname=models.CharField(max_length=255,blank=False)
    accountnumber=models.CharField(max_length=255,blank=False)
    ctcnumber=models.CharField(max_length=255,blank=False)