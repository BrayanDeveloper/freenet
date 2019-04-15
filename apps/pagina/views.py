from django.shortcuts import render, redirect
from apps.pagina.models import Service, Service_plus
# Create your views here.

def index(request):
	statement_services_all = Service.objects.all()
	context = {'statement_services_all': statement_services_all}
	return render(request, 'blosure/index.html', context)

def services(request):
	if request.method == "GET":
		statement_services_all = Service.objects.all()
		statement_services = Service_plus.objects.filter(id_service=request.GET.get('id'))
		context = {'statement_services': statement_services, 'statement_services_all': statement_services_all}
		return render(request, 'blosure/services.html', context)
