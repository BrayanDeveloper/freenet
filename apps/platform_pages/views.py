from django.shortcuts import render
from apps.platform_pages.models import Counter_page
# Create your views here.

def counter(request):
    return render(request, 'platform_pages/contable.html')