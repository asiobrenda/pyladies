from django.shortcuts import render
from django.apps import apps as django_apps
from django.db import connection
from django.http import HttpResponse
from . models import City


def home(request):
    varx = 'HTML DOM ELEMENT- CREATING TABS'

    city = City.objects.all()
    return render(request, 'brenda/index.html', {'varx':varx, 'city':city})
