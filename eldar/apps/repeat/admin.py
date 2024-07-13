from django.contrib import admin
from .models import TennisClub, Author, Books,CDistrict,DistrictValue

@admin.register(TennisClub)
class TennisClubAdmin(admin.ModelAdmin):
    list_display = ['id', 'member_name', 'gender', 'bio', 'date_joined']
    list_filter = ['gender', 'date_joined']



@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'gender']
    list_filter = ['name']

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'author']

@admin.register(CDistrict)
class CDistrictAdmin(admin.ModelAdmin):
    list_display = ['district_name']


@admin.register(DistrictValue)
class DistrictValueAdmin(admin.ModelAdmin):
    list_display = ['district_name', 'year', 'district_value']