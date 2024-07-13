from django.urls import path
from .views import ClientView, CreateClient, ViewClient, UpdateClient


app_name = 'echen'

urlpatterns = [
    path('', ClientView.as_view(), name='Home'),
    path('Createclient/', CreateClient.as_view(), name='create-client'),
    path('Detailclient/<int:pk>', ViewClient.as_view(), name='detail-client'),
    path('Updateclient/<int:pk>', UpdateClient.as_view(), name='update-client'),


]