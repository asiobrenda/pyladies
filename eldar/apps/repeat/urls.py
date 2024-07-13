from django.urls import path
from .views import (home, tables, addmember, view_member, update_member, get_author, district, upload_data)


app_name = 'repeat'

urlpatterns = [
    path('', home, name='Repeat'),
    path('tables/', tables, name='Tables'),
    path('Newmember/', addmember, name='newmember'),
    path('Viewmember/<int:pk>', view_member, name='view-member'),
    path('Updatemember/<int:pk>', update_member, name='update-member'),
    path('author/<int:author_id>', get_author, name='author'),
    path('district/', district, name='district'),
    path('loaddata/', upload_data, name='loaddata'),
]