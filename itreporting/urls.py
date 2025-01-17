from . import views
from users.views import profile, register
from django.urls import path
from .views import (PostListView,
                    PostDetailView, 
                    PostCreateView, 
                    PostUpdateView, 
                    PostDeleteView,)
# from rest_framework import routers


app_name = 'itreporting'

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('policies', views.policies, name='policies'),
    path('regulations', views.regulations, name='regulations'),
    path('contact', views.contact, name='contact'),
#    path('report/', views.report, name='report'),
    path('itreporting/issue_list', PostListView.as_view(), name='reportlist'),
    path('itreporting/issue_detail', PostDetailView.as_view
         (issue_detail.html), name='issue_detail'),
    path('itreporting/issue_create', PostCreateView.as_view
         (issue_create.html), name='create_issue'),
    path('itreporting/issue_update/', PostUpdateView.as_view
         (issue_update.html),
         name='issue-update'),
    path('itreporting/issue_delete', PostDeleteView.as_view
         (issue_delete.html), name='issue_delete'),
#    path('itreporting/send_mail1', views.send_mail1, name='email'),
]
