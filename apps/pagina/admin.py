from django.contrib import admin
from apps.pagina.models import Service, Service_plus, Contact, Appointment, About, Ask_frecuent, Personalization
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

class About_display(admin.ModelAdmin):
    list_display = ['title', 'description']
    list_filter = ['title',]
    search_fields = ['title',]

class Appointment_display(admin.ModelAdmin):
    list_display = ['name', 'message']
    list_filter = ['name','message']
    search_fields = ['name','message']

class AskDisplay(admin.ModelAdmin):
    list_display = ['ask', 'answer']
    list_filter = ['ask',]
    search_fields = ['ask','answer']

class PersonalizationDisplay(admin.ModelAdmin):
    list_display = ['title',]
    list_filter = ['title',]
    search_fields = ['title',]


admin.site.register(Service, Service_display)
admin.site.register(Service_plus, Service_list_display)
admin.site.register(Contact, Contact_display)
admin.site.register(About, About_display)
admin.site.register(Appointment, Appointment_display)
admin.site.register(Ask_frecuent, AskDisplay)
admin.site.register(Personalization, PersonalizationDisplay)