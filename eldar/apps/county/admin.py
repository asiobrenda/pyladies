from django.contrib import admin
from .models import County, CountyValue

@admin.register(County)
class CountyAdmin(admin.ModelAdmin):
    list_display = ['country']
    list_filter = ['country']


@admin.register(CountyValue)
class CountyValueAdmin(admin.ModelAdmin):
    list_display = ['county', 'years', 'value_data']
