from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.views .generic import CreateView, UpdateView
from.models import Category, Project, ProjectImage
from .forms import ProjectForm, PrjectImagesForm
from django.contrib.auth.decorators import login_required
from .models import *




def show_by_category(request, id):
    # category = Category.objects.get(id=id)
    # return render(request,'campaign/showbyCategory.html',{'category':category})
    try:
        category = Category.objects.get(id=id)
        print(category)
        projects = Project.objects.filter(catergory=category)
        print(projects)
        return render(request,'campaign/showbyCategory.html',{'category':category, 'projects' : projects })
    except:
        return render(request, "notfound.html",{'msg':"category Not Found"}) 


def show_all(request):
    try:
        projects=Project.AllProject()
        return render(request,"campaign/showall.html",{'projects':projects})
    except:
        return render(request, "notfound.html",{'msg':"projects Not Found"})

def project_detail(request,project_slug):
    try:
        project=Project.objects.get(slug=project_slug)
        return render(request,"campaign/projectdetail.html",{'project':project})
    except:
        return render(request, "notfound.html",{'msg':"project Not Found"})

@login_required
def delete_project(request,project_slug):
    try:
        project=Project.objects.get(slug=project_slug)
        if project.owner.id == User.id:
            Project.delete_project(id)
            return redirect('showall')
        else:
            return render(request, "notfound.html",{'msg':"You Can't delete  this project!"})
    except:
        return render(request, "notfound.html",{'msg':"project Not Found"})


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
