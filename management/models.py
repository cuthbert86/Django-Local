
from django.db import models
from django.db.models import Count, Model
from django.contrib.auth.models import User
from datetime import datetime, date
from django.utils import timezone
from django.core.validators import MaxValueValidator
from django.conf import settings
from rest_framework import serializers
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _


Category = [("compulsary", "compulsary"),
            ("voluntary", "voluntary")]

available = [("Yes", "Yes"),
             ("No", "No")]


class Module(models.Model):
    name = models.CharField(primary_key=True, max_length=30, default='')
    Course_Code = models.CharField(max_length=10, default='0000')
    credits = models.IntegerField(default=0)
    category = models.CharField(choices=Category, max_length=30)
    Description = models.TextField(max_length=200, default='')
    coursename = models.CharField(max_length=40)
    avalaible = models.CharField(choices=available, max_length=10)

    def __str__(self):
        return f'{self.name} + {self.Course_Code}'

    def get_absolute_url(self):
        return reverse('management/module_details', kwargs={'pk': self.pk})


class Course(models.Model):
    name = models.CharField(
        primary_key=True, max_length=30)
    module = models.ForeignKey(
        Module, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} + {self.module}'


class ModuleCourse(models.Model):
    name = models.ManyToManyField(to=Course)
    module = models.ForeignKey(to=Module, on_delete=models.PROTECT)
    timestamp = models.DateTimeField(default=datetime.now,
                                     primary_key=True)

    def __str__(self):
        return f'{self.name} + {self.module}'


class Registration(models.Model):   
    user = models.ForeignKey(to=User, default=User, on_delete=models.CASCADE)
    Module = models.ForeignKey(to=Module, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(default=datetime.now, null=True)

    def __str__(self):
        return f'{self.user} - {self.Module}'

    def get_absolute_url(self):
        return reverse(
            'management:registration_detail', kwargs={'pk': self.pk})
