from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Module, Course, Registration
from django.contrib.auth.decorators import login_required
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit
from django.utils import timezone
from users.models import Profile


class RegistrationForm(forms.ModelForm):
    model = Registration
    module = forms.ChoiceField(
        choices=[], label='Please select a module from the list')

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['module'].choices = [
            (Module.name) for Module in Module.objects.all()]

    @login_required
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ModuleForm(ModelForm):
    model = Module
    fields = 'name', 'Course_Code', 'credits', 'category',
    'Description', 'available'

    @login_required
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CourseForm(forms.ModelForm):
    model = Course
    module = forms.ChoiceField(
        choices=[], label='Please select a module from the list')

    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        self.fields['module'].choices = [
            (Module.name) for Module in Module.objects.all()]

    @login_required
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
