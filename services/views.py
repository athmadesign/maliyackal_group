from django.shortcuts import render
from .models import Service

def services(requests):
    services = Service.objects.all()
    context = {'services': services}
    return render(requests, 'core/services.html', context)

def service_detail(requests, slug):
    service = Service.objects.get(slug=slug)
    context = {'service': service}
    return render(requests, 'core/service_detail.html', context)