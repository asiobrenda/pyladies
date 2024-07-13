from django.urls import path
from .views import home, tabs, get_data, delete_data, save_content, save_btn, saved_btn

app_name = 'tabs'

urlpatterns = [
    path('', home, name='Home'),
    path('add_tab/', tabs, name='add_tab'),
    path('get_data/', get_data, name='get_data'),
    path('delete_tab/', delete_data, name='delete_tab'),
    path('save_content/', save_content, name='saveContent'),
    path('save_btn/', save_btn, name='save_btn'),
    path('saved_btn/', saved_btn, name='saved_btn'),

]
