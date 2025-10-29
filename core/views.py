from django.shortcuts import render
from .models import Slider, Testimonial


def home(requests):
    sliders = Slider.objects.all()
    testimonials = Testimonial.objects.all()
    context = {'sliders': sliders, 'testimonials': testimonials}
    return render(requests, 'core/index.html', context)

def about(requests):
    testimonials = Testimonial.objects.all()
    context = {'testimonials': testimonials}
    return render(requests, 'core/about.html', context)

def contact(requests):
    return render(requests, 'core/contact.html')

def services(requests):
    return render(requests, 'core/services.html')

def projects(requests):
    return render(requests, 'core/projects.html')

def service_detail(requests):
    return render(requests, 'core/service_detail.html')