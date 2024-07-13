from django.urls import path
from .import views

app_name = 'hangman'

urlpatterns = [
    path('', views.home, name='home'),
    path('play/<int:game_id>',views.play, name='play' )
]