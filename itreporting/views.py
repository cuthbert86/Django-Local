from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.urls import reverse_lazy
from .models import Issue, ContactSubmission
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import DeleteView, UpdateView
import requests
from django.core.mail import send_mail
from itapps import settings
from users.models import Profile
from itreporting.forms import ContactForm, IssueForm
from django.contrib import messages
from django.contrib.auth.models import User


def home(request):
    return render(request, 'itreporting/home.html', {'title': 'Home'})


"""
def home(request):
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
    weather_data.append(weather) # Add the data for the current city into our list

    return render(request, 'itreporting/home.html', {'title': 'Homepage', 'weather_data': weather_data})
"""


def about(request):
    return render(request, 'itreporting/about.html', {'title': 'About'})


def contact(request):
    return render(request, 'itreporting/contact.html', {'title': 'Contact'})


def regulations(request):
    return render(request, 'itreporting/regulations.html', 
                  {'title': 'IT Regulations'})


def policies(request):
    return render(request, 'itreporting/policies.html',
                  {'title': 'IT Policies'})


def successs(request):
    return render(request, 'itreporting/success.html',
                  {'title': 'Submission Successful!'})


class IssueListView(ListView):
    model = Issue
    fields = ['self', 'author', 'date_submitted', 'urgent']
    template_name = 'itreporting/issue_list.html'
    issue = 'issues'
    paginate_by = 5  # Optional pagination

    @login_required
    def get_issue(self):
        return Issue.objects.all()


class IssueDetailView(DetailView):
    model = Issue
    fields = ['type', 'room', 'urgent', 'details']

    @login_required
    def test_func1(self):
        issue = self.get_object()
        return self.request.user(issue)


class IssueCreateView(LoginRequiredMixin, CreateView):
    model = Issue
    fields = ['type', 'room', 'urgent', 'details']
    success_url = 'home'
    template_name = 'issue_create.html'

    @login_required
    def test_func2(self):
        issue = self.get_object()
        return self.request.user == issue.author

    @login_required
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Issue
    fields = ['type', 'room', 'urgent', 'details']
    success_url = 'home'

    @login_required
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class IssueUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Issue
    fields = ['type', 'room', 'details']
    success_url = 'home'
    template_name = 'itreporting/issue_create.html'

    @login_required
    def test_func2(self):
        issue = self.get_object()
        return self.request.user == issue.author


class IssueDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Issue
    form_class = IssueForm
    success_url = 'home'

    @login_required
    def test_func3(self):
        issue = self.get_object()
        return self.request.user == issue.author


class UserIssueListView(ListView):
    model = Issue
    template_name = 'itreporting/user_issues.html'
    context_object_name = 'issues'
    paginate_by = 5

    @login_required
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Issue.objects.filter(author=user).order_by('-date_submitted')


class ContactCreateView(LoginRequiredMixin, CreateView):
    model = ContactSubmission
    fields = ['name', 'email', 'subject', 'message']
    success_url = 'success'
    template_name = 'contact.html'

    @login_required
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, 'Unable to send the enquiry')
        return super().form_invalid(form)

    def get_success_url(self):
        return self.request.path

    @login_required
    def send_mail(request):
        context = {}

        if request.method == 'POST':
            address = request.POST.get('address')
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            if address and subject and message:
                try:
                    send_mail(subject, message, settings.EMAIL_HOST_USER,
                              [address])
                    context['result'] = 'Email sent successfully'
                except Exception as e:
                    context['result'] = f'Error sending email: {e}'
            else:
                context['result'] = 'All fields are required'

        return render(request, "contact_create.html", context)


@login_required
def report(request):
    issues = Issue.objects.all()
    context = {'issues': issues}
    return render(request, 'itreporting/report.html', context)


def success(request):
    return render(request, 'success.html')
