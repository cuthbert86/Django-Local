from django.db import models
from django.db.models import Count, Model
from django.contrib.auth.models import User
from datetime import datetime, date
from django.utils import timezone
# from django.core.validators import MaxValueValidator
from django.conf import settings
# from rest_framework import serializers
from django.urls import reverse


Category = [
   ("compulsary", "compulsary"),
   ("voluntary", "voluntary")
]

available = [
    ("Yes", "Yes"),
    ("No", "No"),
]


class Module(models.Model):
    name = models.CharField(primary_key=True, max_length=30, default='')
    Course_Code = models.CharField(max_length=10, default='0000')
    credits = models.IntegerField(default=0)
    category = models.BooleanField(choices=Category, default="voluntary")
    Description = models.TextField(max_length=200, default='')
    Course = models.CharField(max_length=50, default='')
    avalaible = models.BooleanField(choices=available, default="Yes")

    def __str__(self):
        return f'{self.name} Module in {self.Course}'

    def get_absolute_url(self):
        return reverse('management/module_details', kwargs={'pk': self.pk})


class Course(models.Model):
    name = models.CharField(primary_key=True, max_length=40, default='')
    module = models.ForeignKey(to=Module, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self}'


class Registration(models.Model):
    user = models.ForeignKey(to=User, default=User, on_delete=models.CASCADE)
    Module = models.ForeignKey(Module, on_delete=models.CASCADE)
    registration_date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user} - {self.Module}'
