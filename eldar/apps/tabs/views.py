from django.shortcuts import render
from .models import City, Client
from django.http import JsonResponse


def home(request):
    varx = 'CREATING HTML ELEMENTS USING JAVASCRIPT'

    tab = City.objects.all()

    # if request.method == 'POST':
    #     name_ = request.POST['name']
    #     gender_ = request.POST['gender']
    #
    #     Client.objects.create(name=name_, gender=gender_)

    return render(request, 'tabs/index.html', {'varx': varx, 'tabs':tab})




def tabs(request):
    tab_name = request.POST['dic_']
    #print('type is_', type(tab_name))

    print(type(tab_name))
    dic__ = eval(tab_name)
    print('-----' *20)
    print("type_of_dic_is_", type(dic__))
    name = dic__['city_name']
    color_ = dic__['color']
    description_ = dic__['description']
    tab_name, t = City.objects.get_or_create(city_name=name, color=color_, description=description_)
    print(tab_name.city_name)
    print(tab_name.id)
    dic = {
      'tab_id': tab_name.id,
        'tab_name': tab_name.city_name,
        'tab_content':tab_name.description,
        'tab_color': tab_name.color,
    }

    return JsonResponse(dic)


def get_data(request):
    content = City.objects.all()
    #print(content)
    dic = {}

    for c in content:
        dic[c.id] = {'city_name': c.city_name, 'tab_color': c.color,'tab_content':c.description}
        #print('----'*20)
        #print(dic)
    return JsonResponse(dic)

def delete_data(request):
    delete_content = request.POST['delete_tab_']
    content = City.objects.get(city_name=delete_content)
    tab_id = content.id
    content.delete()
    dic = {
         'tab_id_':tab_id

    }
    return JsonResponse(dic)

def save_content(request):
    tab_id = request.POST['tab_id']
    #print(tab_id)
    content = request.POST['dic_']
    #print(content)
    tab = City.objects.get(id=tab_id)
    tab.description = content
    #print(111111)
    #print(tab.description)
    tab.save()

    dic = {
        'tab_id':tab_id
    }

    return JsonResponse(dic)

def save_btn(request):
    tab_id = request.POST.get('tab_num')
    btn_id = request.POST.get('btn_id')
    tab_name_ = request.POST.get('tab_name')
    save_btn_ = request.POST.get('save_btn1_')

    content = {"btn_" + tab_name_: save_btn_, 'btn_id_':btn_id}

    city = City.objects.get(id=tab_id)

    #Retrieve from python the JSON if it's not there initialize to {}
    saved_data = city.save_btn if city.save_btn else {}

    #Ensure that the saved_data[tab_id] is a list
    if tab_id not in saved_data:
        saved_data[tab_id] = []

    #Append the content
    saved_data[tab_id].append(content)

    #Updating the appended content
    city.save_btn = saved_data
    city.save()
    dic = {}

    return JsonResponse(dic)


def saved_btn(request):
    btn_saved = City.objects.all()

    dic = {}

    #print(dic)

    for b in btn_saved:
        dic[b.id] = b.save_btn

    dic = {'saved_btn': dic}

    #print('--'*40)
    #print(dic)

    return JsonResponse(dic)


