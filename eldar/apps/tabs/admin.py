from django.contrib import admin
from .models import City, Client

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['city_name', 'color', 'description', 'save_btn']

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender']

