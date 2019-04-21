from django.shortcuts import render, redirect
from apps.pagina.models import Service, Service_plus, Contact, Appointment, About, Ask_frecuent, Personalization
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

def index(request):
	statement_services_all = Service.objects.all()
	data_personalization = Personalization.objects.all()
	context = {'statement_services_all': statement_services_all, 'data_personalization': data_personalization}
	return render(request, 'blosure/index.html', context)

def services(request):
	if request.method == "GET":
		statement_services_all = Service.objects.all()
		statement_services = Service_plus.objects.filter(id_service=request.GET.get('id'))
		context = {'statement_services': statement_services, 'statement_services_all': statement_services_all}
		return render(request, 'blosure/services.html', context)
	else:
		statement_services_all = Service.objects.all()
		statement_services = Service_plus.objects.all()
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

		#html_message = render_to_string('template_email/email.html', {'context': context})
		#plain_message = strip_tags(html_message)
		#email_soport = 'ingjavierbuitrago@gmail.com'
		#send_mail('solicitud de contacto', plain_message, settings.EMAIL_HOST_USER,[email_soport], html_message=html_message, fail_silently=False)

		#if mail_send_request:
		#	send_mail('solicitud de contacto', plain_message, settings.EMAIL_HOST_USER,
		#			  [email], html_message=html_message, fail_silently=False)





		return render(request, 'blosure/contact.html', context)
	statement_services_all = Service.objects.all()
	return render(request, 'blosure/contact.html', {'statement_services_all': statement_services_all } )

def appointment(request):
	if request.method == "POST":
		statement_services_all = Service.objects.all()
		statement = Appointment(name=request.POST.get('name'), message=request.POST.get('message'), email=request.POST.get('email'), cel_phone=request.POST.get('phone'), dia=request.POST.get('dia'))
		statement.save()

		dia = request.POST.get('dia')
		phone = request.POST.get('phone')
		email = request.POST.get('email', None)
		message = request.POST.get('message')
		name = request.POST.get('name')
		qqtitle = "Cita agendada por " + name + " a FreenetBusiness"
		context = {'email': email, 'phone':phone, 'dia':dia, 'message': message, 'name':name, 'enviado':'Cita agendada exitosamente', 'statement_services_all': statement_services_all}

		#html_message = render_to_string('template_email/mail_appointment.html', {'context': context})
		#plain_message = strip_tags(html_message)

		#send_priority = send_mail(title, plain_message, settings.EMAIL_HOST_USER,
		#			  ['ganbetacool@gmail.com'], html_message=html_message, fail_silently=False)

		#if send_priority:
		#	send_mail(title, plain_message, settings.EMAIL_HOST_USER,
		#			  [email], html_message=html_message, fail_silently=False)


		return render(request, 'blosure/appointment.html', context)
	statement_services_all = Service.objects.all()
	return render(request, 'blosure/appointment.html', {'statement_services_all': statement_services_all } )


def about(request):
	statement_services_all = Service.objects.all()
	statement_about = About.objects.all()
	context = {'statement_about': statement_about, 'statement_services_all': statement_services_all}
	return render(request, 'blosure/about.html', context)


def services_details(request):
	if request.method == "GET":
		statement_services_all = Service.objects.all()
		statement_services = Service_plus.objects.filter(id=request.GET.get('id'))
		context = {'statement_services': statement_services, 'statement_services_all': statement_services_all}
		return render(request, 'blosure/services_details.html', context)

def search_services(request):
	if request.method == "POST":
		statement_services_all = Service.objects.all()
		statement_services = Service_plus.objects.filter(name_service__contains=request.POST.get('search'), description_service__contains=request.POST.get('search'))
		context = {'statement_services': statement_services, 'statement_services_all': statement_services_all}
		return render(request, 'blosure/search_services.html', context)
	else:
		statement_services_all = Service.objects.all()
		statement_services = Service_plus.objects.all()
		context = {'statement_services': statement_services, 'statement_services_all': statement_services_all}
		return render(request, 'blosure/search_services.html', context)

def ask_frecuent(request):
	statement_services_all = Service.objects.all()
	statement = Ask_frecuent.objects.all()
	context = {'ask_frecuents':statement, 'statement_services_all':statement_services_all}
	return render(request, 'blosure/ask_frecuent.html', context)