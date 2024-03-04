from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *



def show_by_category(request, id):
    try:
        category = Category.get_category(id)
        projects = Project.objects.filter(category=category)
        return render(request,'campagin/showcategory.html',{'category':category,'projects':projects})
    except:
        return render(request, "notfound.html",{'msg':"category Not Found"}) 


def show_all(request):
    try:
        projects=Project.AllProject()
        return render(request,"campaign/showall.html",{'projects':projects})
    except:
        return render(request, "notfound.html",{'msg':"projects Not Found"})

def project_detail(request,title):
    try:
        project=Project.get_project_by_name(title)
        return render(request,"campaign/projectdetail.html",{'project':project})
    except:
        return render(request, "notfound.html",{'msg':"project Not Found"})

@login_required
def delete_project(request,id):
    try:
        project=Project.get_project(id)
        if project.owner.id == User.id:
            Project.delete_project(id)
            return redirect('showall')
        else:
            return render(request, "notfound.html",{'msg':"You Can't delete  this project!"})
    except:
        return render(request, "notfound.html",{'msg':"project Not Found"})





