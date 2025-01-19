from django.contrib import admin
from django.urls import path
from newsapp import views


urlpatterns = [
   path('newsapp/index', views.index, name='index'),
   path('admin/', admin.site.urls),
]
