from django.contrib import admin
from .models import Source, Product, YearData, Cities

@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ['id', 'type']
    list_filter = ['type']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['sitc2', 'description']
    list_filter = ['sitc2', 'description']

@admin.register(YearData)
class YearDataAdmin(admin.ModelAdmin):
    list_display = ['source', 'product', 'year', 'value']
    list_filter = ['source', 'product', 'year', 'value']



@admin.register(Cities)
class CitiesAdmin(admin.ModelAdmin):
    list_display = ['name', 'color', 'description']

