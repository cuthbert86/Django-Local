from django.contrib import admin
from .models import Registration, Module, Course, ModuleCourse


admin.site.register(Module)
admin.site.register(Course)
admin.site.register(Registration)
admin.site.register(ModuleCourse)
