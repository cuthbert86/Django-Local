from django.db import models
from django.db.models import Model
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime


Type = [('Hardware', 'Hardware'),
        ('Software', 'Software')]


class Issue(models.Model):
    type = models.CharField(
        max_length=10, choices=Type)
    room = models.CharField(max_length=10)
    urgent = models.BooleanField(default=False)
    details = models.TextField(max_length=200)
    date_submitted = models.DateTimeField(default=datetime.now)
    author = models.ForeignKey(
        User, related_name='issues', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.type} Issue in {self.room}'

    def get_absolute_url(self):
        return reverse(
            'itreporting:issue_detail', kwargs={'pk': self.pk})


class ContactSubmission(models.Model):
    todaysDate = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=20, default='N/A')
    email = models.EmailField(max_length=20, default='')
    subject = models.CharField(max_length=50, default='')
    message = models.TextField(max_length=300, default='')

    def __str__(self):
        return f'{self.todaysDate} - {self.subject}'
