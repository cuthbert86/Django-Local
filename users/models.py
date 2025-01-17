from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
# from management.models import Module
from django.conf import settings
# from django.db.models import Model
from django.contrib import admin


class Profile(models.Model):
    user = models.OneToOneField(
        User, primary_key=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    StudentOrStaff = models.CharField(max_length=100, choices=[
        ('Student', 'Student'), ('Staff', 'Staff')], default='Student')
    date_of_birth = models.DateField(default=datetime.now)
    address = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=30, default='')
    country = models.CharField(max_length=30, default='')
    image = models.ImageField(default='media/profile_pics/default.jpeg',
                              upload_to='media/profile_pics')
#    Registration_ID = models.ForeignKey(to='management.Registration',
#                                        on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.user.first_name} + {self.user.last_name}'
