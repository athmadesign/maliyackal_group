from django.shortcuts import render
from .models import Project

def projects(requests):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(requests, 'core/projects.html', context)

def project_detail(requests, slug):
    project = Project.objects.get(slug=slug)
    context = {'project': project}
    return render(requests, 'core/project_detail.html', context)