from django.urls import path
from .views import home, truncate_skills

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('truncate/<str:app_label>/<str:table_name>', truncate_skills, name='truncate_table'),

]