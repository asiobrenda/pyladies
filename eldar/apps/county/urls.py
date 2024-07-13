from django.urls import path, include
from .views import home, upload_data


app_name = 'county'

urlpatterns = [
    path('', home, name='Home'),
    path('loaddata', upload_data, name='loaddata'),
    path('core/', include('eldar.apps.core.urls')),
]