"""PROJECTNAME URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from APPNAME import views as v
from contact import views as c

# this import show upload images in browser
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.home, name='home'),
    path('home/', c.home2, name='home2'),
    path('about/', v.about, name='about'),
    path('team/', v.team, name='team'),
    path('detect/', v.detect, name='detect'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # this import show upload images in browser
