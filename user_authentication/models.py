from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=25, unique=True, blank=True, null=True)
    otp = models.IntegerField(null=True, blank=True)
    last_login = models.DateTimeField(null=True, blank=True)
    otp_generated_at = models.DateTimeField(null=True, blank=True)
    REQUIRED_FIELDS = ["email", "password"]

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"