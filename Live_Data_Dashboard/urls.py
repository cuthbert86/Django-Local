from django.urls import path
from .views import node_red_dashboard


urlpatterns = [
    path('node-red-dashboard/', node_red_dashboard, name='node_red_dashboard'),
            # other URL patterns
]
