"""eldar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('eldar.apps.echen.urls')),
    path('r/', include('eldar.apps.repeat.urls')),
    path('ue/', include('eldar.apps.Ueconomics.urls')),
    path('c/', include('eldar.apps.core.urls')),
    path('d/', include('eldar.apps.dataAnalysis.urls')),
    path('t/', include('eldar.apps.tabs.urls')),
    path('b/', include('eldar.apps.brenda.urls')),
    path('cs/', include('eldar.apps.county.urls')),
    path('bt/', include('eldar.apps.buttons.urls')),
    path('ct/', include('eldar.apps.cities.urls')),
    path('blog/', include('eldar.apps.blog.urls')),
    path('h/', include('eldar.apps.hangman.urls')),
    path('posts/', include('eldar.apps.posts.urls')),

]+  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
