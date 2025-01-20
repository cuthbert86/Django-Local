from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic import DeleteView, FormView
from django.core.mail import send_mail
from django.template.loader import get_template
from django.template import Context
import requests
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import DeleteView
from .models import Module, Registration, Course
from django.http import HttpResponse
from .forms import RegistrationForm, ModuleForm, CourseForm
from django.contrib.auth.models import User
from itapps import settings
from django.urls import reverse_lazy
from .models import Module, Registration, Course, ModuleCourse


@login_required
def welcome(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={},{}&units=metric&appid={}'
    cities = [('Sheffield', 'UK'), ('Melaka', 'Malaysia'), ('Bandung', 'Indonesia')]
    weather_data = []
    api_key = 'de13554a89154438878bf77424a0ca05'

    for city in cities:
        city_weather = requests.get(url.format(city[0], city[1], api_key)).json() # Request the API data and convert the JSON to Python data types

    weather = {
        'city': city_weather['name'] + ', ' + city_weather['sys']['country'],
        'temperature': city_weather['main']['temp'],
        'description': city_weather['weather'][0]['description']
    }
    weather_data.append(weather)  # Add the data for the current city into our list

    return render(request, 'management/welcome.html', {'title': 'Welcome', 'weather_data': weather_data})


class CourseListView(ListView):
    model = Course
    courses = Course.objects.all()

    @login_required
    def course_list(request, courses):
        context = {'Courses': courses}
        return render('management/course_list.html', context)


class ModuleListView(ListView):
    model = Module
    modules = Module.objects.all()

    @login_required
    def module_list(request, modules):
        context = {'modules': modules}
        return render('management/module_list.html', context)


class ModuleDetailView(DetailView):
    model = Module
    fields = ['Name', 'Course_Code', 'credits', 'Category', 'Description',
              'available']

    @login_required
    def Module_detail(request, Module):
        context = Module.objects.get()
        if request.method != "POST":
            return HttpResponse("<h2>Method Not Allowed</h2>")
        else:
            Module.name = request.POST.get('Name')
            Module.Course_Code = request.POST.get('Course Code')
            Module.credits = request.POST.get('credits')
            Module.Category = request.POST.get('Category')
            Module.Description = request.POST.get('Description')
#            Module.Course = request.POST.get('Course')
            Module.availabile = request.POST.get('availability')
        return render(request, "management/module_details", context)


class RegistrationListView(ListView):
    model = Registration
    template_name = 'managemenmt/registration_list.html'
    context_object_name = 'registration'

    @login_required
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Registration.objects.filter(
            author=user).order_by('-date_submitted')


def success_view(request):
    return render(request, 'success.html')


class CreateModuleView(CreateView):
    model = Module
    fields = ['Name', 'Course_Code', 'credits', 'Category', 'Description',
              'coursename', 'available']
    success_url = 'management/create_module'

    @login_required
    def module_form(request):
        context = {}
        form = ModuleForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()

        context['module_form'] = form
        return render(request, "module_form.html", context)

    @login_required
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AddCourseView(CreateView):
    model = Course
    fields = ['name', 'module']
    template_name = 'management/add_course.html'
    success_url = 'management/add_course'

    @login_required
    def add_course(self, form, request):
        if request.method == 'POST':
            form = CourseForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(request, 'management/add_course')
        else:
            form = CourseForm()
        return render(request, 'management/add_course.html', {'form': form})


class RegistrationFormView(LoginRequiredMixin, FormView):
    model = Registration
    template_name = 'management/registration_form.html'
    success_url = 'management/success'

    @login_required
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AddModuleView(CreateView):
    model = Module
    fields = ['Name', 'Course_Code', 'credits', 'Category', 'Description',
              'Course', 'available']
    success_url = 'management/add_module'

    @login_required
    def add_module(self, form, request):
        if request.method == 'POST':
            form = ModuleForm(request.POST or None)
        if form.is_valid():
            form.save()  # Save the module to the database
            return redirect(request, 'add_module')  # Redirect to the module list page or any other page
        else:
            form = ModuleForm()

        return render(request, 'add_module.html', {'form': form})
