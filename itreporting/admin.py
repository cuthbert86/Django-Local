from django.contrib import admin
from .models import Issue, ContactSubmission
from users.models import User, Profile


# Register your models here.
admin.site.register(Issue)
admin.site.register(ContactSubmission)
