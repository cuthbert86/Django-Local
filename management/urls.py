from django.contrib import admin
from django.urls import path, include, reverse_lazy
from . import views as student_views
from django.contrib.auth.models import User
from .views import ModuleDetailView, welcome, ModuleListView
from .views import RegistrationFormView, success_view
from .views import AddCourseView, CourseListView, AddModuleView

urlpatterns = [
    path('management/welcome', welcome, name='welcome'),
    path('management/module_list', ModuleListView.as_view(
        template_name='module_list.html'), name='module_list'),
    path('management/module_details', ModuleDetailView.as_view(
        template_name='module_details.html'), name='module_details'),
    path('management/registration', RegistrationFormView.
         as_view(template_name='registration.html'),
         name='registration'),
    path('management/success', success_view, name='success'),
#    path('management/create_module', CreateModuleView.as_view(
#         template_name='create_module.html'), name='create_module'),
    path('management/add_course', AddCourseView.as_view(
        template_name='_course.html'), name='add_course'),
    path('management/course_list', CourseListView.as_view(
        template_name='course_list.html'), name='course_list'),
    path('mangemnt/add_module', AddModuleView.as_view(
        template_name='add_module.html'), name='add_module'),

]