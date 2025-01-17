from . import views
from users.views import profile, register
from django.urls import path, include
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    UserPostListView)
# from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from .forms import IssueForm, ContactForm


app_name = 'itreporting'

urlpatterns = [
    path('', views.home, name='home'),
    path('itreporting/issue_list', views.PostListView.as_view(
        template_name='issue_list.html'), name='issue_list'),
    path('itreporting/issue_detail', views.PostDetailView.as_view(
        template_name='issue_detail.html'), name='issue_detail'),
    path('itreporting/create_issue', views.PostCreateView.as_view(
        template_name='create_issue.html'), name='create_issue'),
    path('itreporting/issue_update', views.PostUpdateView.as_view(
        template_name='issue_update.html'), name='issue_update'),
    path('itreporting/issue_delete', views.PostDeleteView.as_view(
        template_name='issue_delete.html'), name='issue_delete'),
#    path('itreporting/send_mail1', views.send_mail1, name='email'),
    path('itreporting/issue/<str:username>', UserPostListView.as_view(
        template_name='user_issues.html'), name='user_issues'),
]
