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


def custom_404(request, exception):
    return render(request, 'core/404.html', status=404)