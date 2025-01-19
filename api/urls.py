from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IssueViewSet
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'api'

router = DefaultRouter()

router.register('issues', IssueViewSet)

urlpatterns = [ 
    path('', include(router.urls)),
    path('auth', obtain_auth_token, name='api_token_auth'),
]
