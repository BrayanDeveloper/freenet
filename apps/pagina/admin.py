from django.contrib import admin
from apps.pagina.models import Service, Service_plus, Contact
# Register your models here.

class Service_display(admin.ModelAdmin):
    list_display = ['name_service', 'description_service', 'link_service']
    list_filter = ['name_service', 'description_service']
    search_fields = ['name_service', 'link_service']

class Service_list_display(admin.ModelAdmin):
    list_display = ['name_service', 'description_service', 'link_service', 'id_service']
    list_filter = ['name_service', 'description_service']
    search_fields = ['name_service', 'link_service']

class Contact_display(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']
    list_filter = ['name', 'email', 'message']
    search_fields = ['name', 'email', 'message']


admin.site.register(Service, Service_display)
admin.site.register(Service_plus, Service_list_display)
admin.site.register(Contact, Contact_display)