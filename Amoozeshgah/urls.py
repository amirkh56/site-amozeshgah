"""
URL configuration for Amoozeshgah project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from debug_toolbar.toolbar import debug_toolbar_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'), name = ''),
    path('accounts/', include('accounts.urls'), name= 'accounts'),
    path('courses/', include('courses.urls'), name = 'courses'),
    path('educational/', include('educational.urls'), name='educational'),
    path('learningcalender/', include('learningcalender.urls'), name='calender'),
] + debug_toolbar_urls()
