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
from .forms import RegistrationForm, ModuleForm, CourseForm, ModuleCourseForm
from django.contrib.auth.models import User
from itapps import settings
from django.urls import reverse_lazy
from .models import Module, Registration, Course, ModuleCourse
from django.forms import formset_factory


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
            context.name = request.POST.get('Name')
            context.Course_Code = request.POST.get('Course_Code')
            context.credits = request.POST.get('credits')
            context.Category = request.POST.get('Category')
            context.Description = request.POST.get('Description')
#            Module.Course = request.POST.get('Course')
            context.availabile = request.POST.get('availability')
        return render(request, "management/module_details", context)


class RegistrationListView(ListView):
    model = Registration
    template_name = 'managemenmt/registration_list.html'
    context_object_name = 'registration'

    @login_required
    def get_queryset(self):
        user = get_object_or_404(to=User, username=self.kwargs.get('username'))
        return Registration.objects.filter(
            author=user).order_by('date_submitted')


def success_view(request):
    return render(request, 'success.html')


class CreateModuleView(CreateView):
    model = Module
    fields = ['Name', 'Course_Code', 'credits', 'Category', 'Description',
              'Course', 'available']
    success_url = 'management/success'

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


class CreateCourseView(LoginRequiredMixin, CreateView):
    model = Course
    fields = ['course_name']
    template_name = 'management/create_course.html'
    success_url = 'management/course_list'

    @login_required
    def course_form(request):
        context = {}
        form = CourseForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()

            context['course_form'] = form
        return render(request, 'course_form.html', context)

    @login_required
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class RegistrationFormView(LoginRequiredMixin, FormView):
    model = Registration
    template_name = 'management/registration_form.html'
    success_url = 'management/success'

    @login_required
    def registration_formset(request):
        context = {}
        registrationformset = formset_factory(RegistrationForm, extra=4)
        if registrationformset.is_valid():
            registrationformset.save()
            context['registration_formset'] = registrationformset
        return render(request, 'generic_formset.html', context)


@login_required
def module_form(request):
    context = {}
    form = ModuleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        context['module_form'] = form
    return render(request, "module_form.html", context)


@login_required
def course_form(request):
    context = {}
    form = CourseForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

        context['course_form'] = form
    return render(request, "course_form.html", context)


@login_required
def module_course_formset(request):
    context = {}
    courseformset = formset_factory(ModuleCourseForm, extra=5)
    if courseformset.is_valid():
        courseformset.save()
        context['module_course_formset'] = courseformset
    return render(request, 'module_course_form.html', context)


@login_required
def module_course_list(request):
    modulecourses = ModuleCourse.objects.all()
    return render(request, 'module_course_list.html',
                  {'module_course': modulecourses})


@login_required
def course_formset_view(request):
    context = {}
    courseFormSet = formset_factory(CourseForm, extra=5)
    formset = courseFormSet(request.POST or None)
    context['courseFormSet'] = formset
    return render(request, "generic_formset.html", context)


@login_required
def module_form_view(request):
    context = {}
    ModuleFormSet = formset_factory(ModuleForm, extra=5) 
    formset = ModuleFormSet(request.POST or None)
    context['module_formset'] = formset
    return render(request, "generic_formset.html", context)
