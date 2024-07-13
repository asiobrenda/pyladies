from django.urls import path
from .views import home

app_name = 'brenda'

urlpatterns = [
    path('', home, name='home'),

]