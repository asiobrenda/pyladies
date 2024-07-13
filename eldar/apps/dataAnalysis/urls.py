from django.urls import path
from .views import home, upload_data

app_name = 'dataAnalysis'

urlpatterns = [
    path('', home, name='home'),
    path('loaddata/', upload_data, name='data')


]