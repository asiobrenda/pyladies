from django.urls import path
from .views import home, news


app_name = 'blog'

urlpatterns = [
    path('', home, name='home'),
    path('news/<int:title_id>/', news, name='news')
]