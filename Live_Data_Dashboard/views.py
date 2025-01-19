from django.shortcuts import render

# Create your views here.

from django.shortcuts import render


def node_red_dashboard(request):
    return render(request, 'node_red_dashboard.html')