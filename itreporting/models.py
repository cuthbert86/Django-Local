from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime

# Create your models here.


class Issue(models.Model):
    type = models.CharField(
        max_length=100, choices=[(
            'Hardware', 'Hardware'), ('Software', 'Software')])
    room = models.CharField(max_length=100)
    urgent = models.BooleanField(default=False)
    details = models.TextField()
    date_submitted = models.DateTimeField(default=datetime.now)
    description = models.TextField()
    author = models.ForeignKey(
        User, related_name='issues', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.type} Issue in {self.room}'

    def get_absolute_url(self):
        return reverse(
            'itreporting:issue-detail', kwargs={'pk': self.pk})
