from . import views
from users.views import profile, register
from django.urls import path
from .views import (PostListView,
                    PostDetailView, 
                    PostCreateView, 
                    PostUpdateView, 
                    PostDeleteView,)
# from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static


app_name = 'itreporting'

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('policies', views.policies, name='policies'),
    path('regulations', views.regulations, name='regulations'),
    path('contact', views.contact, name='contact'),
#    path('report/', views.report, name='report'),
    path('itreporting/issue_list', views.PostListView.as_view(
        template_name='issue_list.html'), name='issue_list'),
    path('itreporting/issue_detail', views.PostDetailView.as_view(
        template_name='issue_detail.html'), name='issue_detail'),
    path('itreporting/issue_create', views.PostCreateView.as_view(
        template_name='issue_create.html'), name='create_issue'),
    path('itreporting/issue_update/', views.PostUpdateView.as_view(
        template_name='issue_update.html'), name='issue-update'),
    path('itreporting/issue_delete', views.PostDeleteView.as_view(
        template_name='issue_delete.html'), name='issue_delete'),
#    path('itreporting/send_mail1', views.send_mail1, name='email'),
]
