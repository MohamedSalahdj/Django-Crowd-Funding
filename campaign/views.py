from django.shortcuts import render
from django.contrib.auth.models import User
from django.views .generic import CreateView, UpdateView

from.models import Category, Project, ProjectImage
from .forms import ProjectForm, PrjectImagesForm




def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form =  form.save(commit=False)
            form.owner = request.user
            form.save()
            # form.save_m2m()
    else:
        form = ProjectForm()

    context = {'form':form}
    return render(request, 'campaign/create_project.html', context)


def update_project(request, project_slug):
    project = Project.objects.get(slug=project_slug)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form =  form.save(commit=False)
            form.owner = request.user
            form.save()
            # form.save_m2m()
    else:
        form = ProjectForm(instance=project)

    context = {'form':form}
    return render(request, 'campaign/update_project.html', context)
