from django.shortcuts import render
from django.db import connection
from homepages.models import DonutInfo

# Create your views here.

def indexPageView(request):
    donuts = DonutInfo.objects.all()
    data = {
        'donuts': donuts
    }

    return render(request, 'homepages/index.html', data)