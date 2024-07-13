from django.urls import path
from .views import home, tabs, get_data, delete_data, save_data, save_btn, saved_btn, saved_btn_code, get_saved_btn_code, delete_saved_btn

app_name = 'cities'

urlpatterns = [
    path('', home, name='Cities'),
    path('tabs/', tabs, name='Tabs'),
    path('get_data/', get_data, name='Get_data'),
    path('delete_data/', delete_data, name='Delete'),
    path('save_data/', save_data, name='Save'),
    path('save_btn', save_btn, name='Save_btn'),
    path('saved_btn', saved_btn, name='Saved_btn'),
    path('saved_btn_code', saved_btn_code, name='Saved_btn_code'),
    path('get_saved_btn_code', get_saved_btn_code, name='get_Saved_btn_code'),
    path('delete_saved_btn', delete_saved_btn, name='delete_saved_btn'),

    #path('update_tab/<str:tab_id>/', update_tab, name='update_tab'),

]