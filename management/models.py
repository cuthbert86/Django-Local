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


Category = [("compulsary", "compulsary"),
            ("voluntary", "voluntary")]

available = [("Yes", "Yes"),
             ("No", "No")]


class Module(models.Model):
    name = models.CharField(primary_key=True, max_length=30, default='')
    Course_Code = models.CharField(max_length=10, default='0000')
    credits = models.IntegerField(default=0)
    category = models.CharField(choices=Category, max_length=10)
    Description = models.TextField(max_length=200, default='')
#    course_name = models.ForeignKey(Course, on_delete=models.PROTECT)
    avalaible = models.CharField(choices=available, max_length=10)

    def __str__(self):
        return f'{self.name}'
    
#    def get_absolute_url(self):
#        return reverse('management/module_details', kwargs={'pk': self.pk})


class Course(models.Model):
    name = models.CharField(
        primary_key=True, max_length=10)

    def __str__(self):
        return f'{self.name}'


class ModuleCourse(models.Model):
    course_name = models.ForeignKey(to=Course, on_delete=models.CASCADE)
    module = models.ForeignKey(to=Module, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.course_name} - {self.module.name}'


class Registration(models.Model):
    user = models.ForeignKey(to=User, default=User, on_delete=models.CASCADE)
    Module = models.ForeignKey(to=Module, on_delete=models.CASCADE)
    registration_date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user} - {self.Module}'
