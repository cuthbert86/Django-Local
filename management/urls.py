from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.contrib.auth.models import User
from .views import ModuleDetailView, welcome, ModuleListView
from .views import RegistrationFormView, success_view, CreateModuleView
from .views import CreateCourseView, CourseListView, module_form
from management import views as student_views


urlpatterns = [
    path('management/welcome', welcome, name='welcome'),
    path('module_list', ModuleListView.as_view(
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
    path('mangemnt/module_form', module_form, name='module_form'),
    path('mangemnt/module_course_formset', student_views.module_course_formset,
         name='module_course_form'),
    path('management/course_formset', student_views.course_formset_view,
         name='course_form'),
]
