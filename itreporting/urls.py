from . import views
from users.views import profile, register
from django.urls import path, include
from .views import IssueListView, IssueDetailView, IssueCreateView
from .views import IssueUpdateView, IssueDeleteView, UserIssueListView
from .views import ContactCreateView, success
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
# from .forms import IssueForm, ContactForm
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views


app_name = 'itreporting'

urlpatterns = [
    path('', views.home, name='home'),
    path('itreporting/issue_list', IssueListView.as_view(
        template_name='itreporting/issue_list.html'), name='issue_list'),
    path('itreporting/issue_detail', IssueDetailView.as_view(
        template_name='itreporting/issue_detail.html'), name='issue_detail'),
    path('itreporting/issue_create', IssueCreateView.as_view(
        template_name='itreporting/issue_create.html'), name='issue_create'),
    path('itreporting/issue_update', IssueUpdateView.as_view(
        template_name='itreporting/issue_update.html'), name='issue_update'),
    path('itreporting/issue_delete', IssueDeleteView.as_view(
        template_name='itreporting/issue_delete.html'), name='issue_delete'),
    path('itreporting/send_mail', views.send_mail, name='email'),
    path('itreporting/user_issues/<str:username>', UserIssueListView.as_view(
        template_name='user_issues.html'), name='user_issues'),
    path('itreporting/issue_create', IssueCreateView.as_view(
        template_name='issue_create.html'), name='issue_create'),
    path('itreporting/contact_create', ContactCreateView.as_view(
        template_name='itreporting/contact_create.html'), name='contact'),
    path('itreporting/success', success, name='success'),
]
