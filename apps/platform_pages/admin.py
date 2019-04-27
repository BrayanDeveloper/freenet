from django.contrib import admin
from apps.platform_pages.models import Counter_page, Caracteristicas, Plan
# Register your models here.
class DisplayCounterPage(admin.ModelAdmin):
    list_display = ['title1',]

class DisplayCaracteristicas(admin.ModelAdmin):
    list_display = ['caracteristicas_title',]

class DisplayPlanes(admin.ModelAdmin):
    list_display = ['plan_title',]


admin.site.register(Counter_page, DisplayCounterPage)
admin.site.register(Caracteristicas, DisplayCaracteristicas)
admin.site.register(Plan, DisplayPlanes)