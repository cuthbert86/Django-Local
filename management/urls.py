from django.contrib import admin
from django.urls import path, include, reverse_lazy
# from . import views as student_views
from django.contrib.auth.models import User
from .views import ModuleDetailView, welcome, ModuleListView
from .views import RegistrationFormView, success_view, CreateModuleView
from .views import CreateCourseView, CourseListView


urlpatterns = [
    path('management/welcome', welcome, name='welcome'),
    path('management/module_list', ModuleListView.as_view(
        template_name='module_list.html'), name='module_list'),
    path('management/module_details', ModuleDetailView.as_view(
        template_name='module_details.html'), name='module_details'),
    path('management/registration_form', RegistrationFormView.
         as_view(template_name='registration_form.html'),
         name='registration_form'),
    path('management/success', success_view, name='success'),
    path('management/create_module', CreateModuleView.as_view(
         template_name='create_module.html'), name='create_module'),
    path('management/create_course', CreateCourseView.as_view(
        template_name='create_course.html'), name='create_course'),
    path('management/course_list', CourseListView.as_view(
        template_name='course_list.html'), name='course_list'),
]
