from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now

class User(AbstractUser):
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')], blank=True)
    birth_date = models.DateField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Timer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def is_active(self):
        return now() < self.end_time