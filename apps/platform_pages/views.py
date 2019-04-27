from django.shortcuts import render
from apps.platform_pages.models import Counter_page, Caracteristicas, Plan
from apps.pagina.models import Service, Slider_setting, Footer
from apps.personalization.models import Menu
# Create your views here.

def counter (request):
    statement_services_all = Service.objects.all()
    data_personalization = Slider_setting.objects.all()
    id_page_counter = Counter_page.objects.filter(for_page='contable')
    for id_p in id_page_counter:
         id_page = id_p.id
    data_caracteristicas = Caracteristicas.objects.filter(id_counter_page=id_page)
    data_planes = Plan.objects.filter(id_counter_page=id_page)
    
    data_footer = Footer.objects.all()
    data_page_counter = Counter_page.objects.all()
    data_menu = Menu.objects.all()

    context = { 'statement_services_all': statement_services_all, 'data_page_counter': data_page_counter, 'data_footer':data_footer, 'data_menu':data_menu, 'data_caracteristicas':data_caracteristicas, 'data_planes':data_planes }
    return render(request, 'platform_pages/contable.html', context)
    
