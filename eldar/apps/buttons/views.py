from django.shortcuts import render
from .models import Tabs
from django.http import JsonResponse

def home(request):
    varx = "CREATING TABS USING JAVASCRIPT"
    tabs = Tabs.objects.all()

    return render(request, 'buttons/index.html',{'varx':varx, 'tabs':tabs})

def add_tab(request):
    tab_name_ = request.POST['dic']
    dic_ = eval(tab_name_)
    name = dic_['cityName']
    description = dic_['description']
    print(111)
    print(description)
    color = dic_['color']
    c, t = Tabs.objects.get_or_create(name=name, description=description, color=color)
    print(t)
    print(c.id)
    print(c)
    dic = {
        'tab_id': c.id,
        'name': c.name,
        'description': c.description,
        'color': c.color
    }
    print('---' * 10)
    # print(dic)
    return JsonResponse(dic)

def get_data(request):
    data = Tabs.objects.all()
    # print(content)
    dic = {}

    for c in data:
        dic[c.id] = {'name': c.name, 'description': c.description, 'color': c.color}
    return JsonResponse(dic)