"""business URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from apps.pagina.views import index, services, contact, appointment, about, services_details, search_services, ask_frecuent, team_unit
from apps.platform_pages.views import counter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('services/', services, name="services"),
    path('contact/', contact, name="contact"),
    path('appointment/', appointment, name="appointment"),
    path('about/', about, name="about"),
    path('services_details/', services_details, name="services_details"),
    path('search_services/', search_services, name="search_services"),
    path('ask_frecuent/', ask_frecuent, name="ask_frecuent"),
    path('team_unit/', team_unit, name="team_unit"),
    path('counter/', counter, name="counter"),
]

