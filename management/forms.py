from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Module, Course, Registration, ModuleCourse
from django.contrib.auth.decorators import login_required
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit
from django.utils import timezone
from users.models import Profile


class RegistrationForm(forms.ModelForm):
    model = Registration
    module = forms.ChoiceField(
        choices=[], label='Please select a module from the list')
    
    @login_required
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['module'].choices = [
            (Module.name) for Module in Module.objects.all()]

    @login_required
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ModuleForm(forms.ModelForm):
    model = Module
    fields = 'name', 'Course_Code', 'credits', 'course', 'category', 'description', 'available'
    course = forms.ChoiceField(
        choices=[], label='Please select a course from the list')

    @login_required
    def __init__(self, *args, **kwargs):
        super(ModuleForm, self).__init__(*args, **kwargs)
        self.fields['course'].choices = [
            (Course.name) for Course in Course.objects.all()]

    @login_required
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CourseForm(forms.ModelForm):

    class Meta:
        Model = Course
        fields = ['name', 'module']
        module = forms.ChoiceField(
            choices=[], label='Please select a module from the list')

    @login_required
    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        self.fields['module'].choices = [
            (Module.name) for Module in Module.objects.all()]

        @login_required
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.layout = Layout(
                Fieldset(
                    'name',
                    'module',
                    ),
                Submit('submit', 'Submit', css_class='button white'),
            )


class ModuleCourseForm(forms.ModelForm):
    model = ModuleCourse
    module = forms.ChoiceField(
        choices=[], label='Please select a module from the list')
    course = forms.ChoiceField(
        choices=[], label='Please select a course from the list')

    @login_required
    def __init__(self, *args, **kwargs):
        super(ModuleCourseForm, self).__init__(*args, **kwargs)
        self.fields['module'].choices = [
            (Module.name) for Module in Module.objects.all()]    
    
    login_required
    def __init__(self, *args, **kwargs):
        super(ModuleCourseForm, self).__init__(*args, **kwargs)
        self.fields['course'].choices = [
            (Course.name) for Course in Course.objects.all()]

    @login_required
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

