from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


Student_CHOICES = (
    ("1", "Student"),
    ("2", "Staff")
)


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email address',
                             help_text='Your SHU email address.')
    StudentOrStaff = forms.ChoiceField(choices=Student_CHOICES, label='Are you a Student or Staff?')
    date_of_birth = forms.DateField(label='Date of Birth: YYYY-MM-DD')
    address = forms.CharField(label='Address')
    city = forms.CharField(label='City')
    country = forms.CharField(label='Country')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email']


class ProfileUpdateForm(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = Profile
        fields = ['image']
