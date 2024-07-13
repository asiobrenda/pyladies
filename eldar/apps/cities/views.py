from django.shortcuts import render
from .models import Cities
from django.http import JsonResponse, HttpResponseBadRequest




def home(request):
    cities_ = "Welcome to Cities"
    city_ = Cities.objects.all()

    return render(request, 'cities/index3.html', {'cities': cities_, 'city': city_})


def tabs(request):

    tab_name_ = request.POST.get('dic')
    dic_ = eval(tab_name_)
    name = dic_['cityName']
    description = dic_['description']
    color = dic_['color']


    c, t = Cities.objects.get_or_create(city_name=name, description=description, color=color)
    print(t)
    print(c.id)
    dic = {
        'tab_id': c.id,
        'city_name': c.city_name,
        'description': c.description,
        'color': c.color
    }
    return JsonResponse(dic)


def get_data(request):

    content = Cities.objects.all()
    #print(content)
    dic = {}

    for c in content:
        dic[c.id] = {'city_name': c.city_name, 'description': c.description, 'color': c.color, 'save_btn': c.save_btn}
        #print(dic)
    return JsonResponse(dic)


def delete_data(request):
    del_content = request.POST['delTab']
    content = Cities.objects.get(city_name=del_content)
    tab_id = content.id
    content.delete()
    dic = {

        'tab_id_': tab_id
    }

    return JsonResponse(dic)


def save_data(request):
    content_id = request.POST['tab_id']
    print(content_id)
    saved_content = request.POST['dic_']
    print(11111)
    print(saved_content)
    content = Cities.objects.get(id=content_id)
    content.description = saved_content
    content.save()

    dic = {
         'content': saved_content,
    }
    print('----'*10)
    print(dic)
    return JsonResponse(dic)



def save_btn(request):
    tab_id = request.POST.get('tab_id')
    btn_id = request.POST.get('copied_btn_id')
    tab_name_ = request.POST.get('tab_name')
    saved_btn = request.POST.get('saved_btn')

    #content = {tab_id: {"tab_" + tab_name_: saved_btn}}

    city = Cities.objects.get(id=tab_id)

    saved_data = city.save_btn if city.save_btn else {}

    if tab_id not in saved_data:
        saved_data[tab_id] = []

    saved_data[tab_id].append({"tab_"+tab_name_: saved_btn, "btn_id": btn_id, "btn_code":""})
    #print(saved_data)

    city.save_btn = saved_data
    city.save()

    dic = {'tab_id': tab_id, 'tab_name': city.city_name}

    return JsonResponse(dic)



def saved_btn(request):

    saved_btn_ = Cities.objects.all()

    dic = {}

    for s in saved_btn_:
        dic[s.id] = s.save_btn

    dic = {"saved_btn_": dic}
    # print("----" * 40)
    # print(dic)

    return JsonResponse(dic)


def saved_btn_code(request):
    tab_id = request.POST.get('tab_id__')
    btn_code = request.POST.get('btn_code')
    btn_id__= request.POST.get('btn_id__')

    #print(tab_id)
    #print(btn_code)
    #print(btn_id__)

    code = Cities.objects.get(id=tab_id)
    code_btn = code.save_btn.get(tab_id, [])
    #print(code_btn)
    for c in code_btn:
        if c.get('btn_id') == btn_id__:
            c['btn_code'] = btn_code

    code.save_btn[tab_id] = code_btn
    #print(code.save_btn[tab_id])
    code.save()

    dic = {}
    for i in code_btn:
        dic[i.get('btn_id')] = i.get('btn_code')
        print(dic)


    return JsonResponse(dic)

def get_saved_btn_code(request):

    saved_btn_ = Cities.objects.all()

    dic = {}

    for s in saved_btn_:
        dic[s.id] = s.save_btn

    dic = {"saved_btn_": dic}
    # print("----" * 40)
    # print(dic)

    return JsonResponse(dic)

def delete_saved_btn(request):
    tab_id = request.POST.get('del_tab_id')
    btn_id = request.POST.get('del_btn_id')
    btn_name = request.POST.get('del_tab_name')


    print(tab_id)
    print(btn_id)

    d = Cities.objects.get(id=tab_id)
    del_code = d.save_btn.get(tab_id, [])
    print(del_code)

    updated_del_btn = [t for t in del_code if t.get('btn_id') != btn_id]

    d.save_btn[tab_id] = updated_del_btn
    d.save()


    return JsonResponse({})

