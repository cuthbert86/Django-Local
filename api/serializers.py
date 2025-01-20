from rest_framework.serializers import ModelSerializer, ReadOnlyField
from itreporting.models import Issue
from management.models import Module, ModuleCourse, Course, Registration


class IssueSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.username') 

    class Meta:
        model = Issue
        fields = [
            'type', 'room', 'urgent', 'details', 'date_submitted', 'author']


class ModuleSerializer(ModelSerializer):

    class Meta:
        model = Module
        fields = ['name', 'Course_Code', 'credits', 'category', 'Description',
                  'avalaible']


class ModuleCourseSerializer(ModelSerializer):

    class Meta:
        model = ModuleCourse
        fields = ['course_name', 'module']


class CourseSerializer(ModelSerializer):

    class Meta:
        model = Course
        fields = ['course_name']


class RegistrationSerializer(ModelSerializer):

    class Meta:   
        model = Registration
        fields = ['user', 'module', 'registration_date']
