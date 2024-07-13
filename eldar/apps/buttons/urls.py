from django.urls import path
from .views import home, add_tab, get_data

app_name = 'buttons'

urlpatterns = [
    path('', home, name='home'),
    path('addtab', add_tab, name='AddTab'),
    path('get_data', get_data, name='getData'),

]

