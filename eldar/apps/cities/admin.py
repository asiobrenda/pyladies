from django.contrib import admin
from .models import Cities

@admin.register(Cities)
class CityAdmin(admin.ModelAdmin):
    list_display = ['city_name', 'color', 'description', 'save_btn']

