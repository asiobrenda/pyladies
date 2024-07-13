from django.shortcuts import render
from .models import Cities
from django.db import IntegrityError
from django.http import JsonResponse, HttpResponseBadRequest




def home(request):
    cities_ = "Welcome to Cities"


    return render(request, 'Ueconomics/index.html', {'cities': cities_})


def tabs(request):
    tab_name_ = request.POST['dic']
    dic_ = eval(tab_name_)
    name = dic_['cityName']
    description = dic_['description']
    color = dic_['color']
    c, t = Cities.objects.get_or_create(name=name, description=description, color=color)
    print(t)
    print(c.id)
    print(c)
    dic = {
        'tab_id': c.id,
        'name': c.name,
        'description': c.description,
        'color': c.color
    }
    print('---'*10)
    #print(dic)
    return JsonResponse(dic)

def get_data(request):

    content = Cities.objects.all()
    #print(content)
    dic = {}

    for c in content:
        dic[c.id] = {'city_name': c.name, 'description': c.description, 'color': c.color}
        #print(dic)
    return JsonResponse(dic)

