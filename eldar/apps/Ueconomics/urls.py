from django.urls import path
from .views import home, tabs,get_data

app_name = 'Ueconomics'

urlpatterns = [
    path('', home, name='home'),
    path('tabs/', tabs, name='Tabs'),
    path('get_data/', get_data, name='Get_data'),
    #path('delete_data/', delete_data, name='Delete'),

]