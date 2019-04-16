from django.shortcuts import render, redirect
from apps.pagina.models import Service, Service_plus, Contact
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.core.mail import send_mail
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

def contact(request):
	if request.method == "POST":
		statement_services_all = Service.objects.all()
		statement = Contact(name=request.POST.get('name'), message=request.POST.get('message'), email=request.POST.get('email'),)
		statement.save()

		email = request.POST.get('email', None)
		message = request.POST.get('message')
		name = request.POST.get('name')
		context = {'email': email, 'message': message, 'name':name, 'enviado':'enviado con exito', 'statement_services_all': statement_services_all}

		html_message = render_to_string('template_email/email.html', {'context': context})
		plain_message = strip_tags(html_message)

		mail_send_request = send_mail('solicitud de contacto', plain_message, settings.EMAIL_HOST_USER,
				  ['ganbetacool@gmail.com'], html_message=html_message, fail_silently=False)

		if mail_send_request:
			send_mail('solicitud de contacto', plain_message, settings.EMAIL_HOST_USER,
					  [email], html_message=html_message, fail_silently=False)





		return render(request, 'blosure/contact.html', context)
	statement_services_all = Service.objects.all()
	return render(request, 'blosure/contact.html', {'statement_services_all': statement_services_all } )

