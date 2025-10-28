from django.shortcuts import render


# Create your views here.

def home(requests):
    return render(requests, 'core/index.html')

def about(requests):
    return render(requests, 'core/about.html')

def contact(requests):
    return render(requests, 'core/contact.html')

def services(requests):
    return render(requests, 'core/services.html')

def projects(requests):
    return render(requests, 'core/projects.html')