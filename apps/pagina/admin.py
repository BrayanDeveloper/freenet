from django.contrib import admin
from apps.pagina.models import Service, Service_plus
# Register your models here.

class Service_display(admin.ModelAdmin):
    list_display = ['name_service', 'description_service', 'link_service']
    list_filter = ['name_service', 'description_service']
    search_fields = ['name_service', 'link_service']

class Service_list_display(admin.ModelAdmin):
    list_display = ['name_service', 'description_service', 'link_service', 'id_service']
    list_filter = ['name_service', 'description_service']
    search_fields = ['name_service', 'link_service']


admin.site.register(Service, Service_display)
admin.site.register(Service_plus, Service_list_display)