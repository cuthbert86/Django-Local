from django import forms
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Profile
from .models import Issue, ContactSubmission
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit
from django.utils import timezone


@login_required
class ContactForm(forms.ModelForm):
    model = ContactSubmission
    name = forms.CharField(max_length=30, label='Name')
    email = forms.EmailField(label='Email')
    subject = forms.CharField(label='Subject', max_length=50)
    message = forms.CharField(label='Message', widget=forms.Textarea)

    def send_mail(self):
        send_mail(self.cleaned_data.get('subject') + ', sent on behalf of ' +
                  self.cleaned_data.get('name'),
                  self.cleaned_data.get('message'),
                  self.cleaned_data.get('email'),
                  ['bainescuthbert@gmail.com'])


@login_required
class IssueForm(forms.ModelForm):
    class Meta:
        Model = Issue
        fields = ['type', 'room', 'urgent', 'details']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.layout = Layout(
                Fieldset(
                    'type',
                    'room',
                    'urgent',
                    'detai;s',
                    ),
                Submit('submit', 'Submit', css_class='button white'),
                )
