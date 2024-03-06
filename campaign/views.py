from django.shortcuts import render,redirect, reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .models import Category, Project, ProjectImage, Review, Donate
from .forms import ProjectForm, ProjectImagesForm, ReviewForm, DonateForm
from django.db.models import Sum


class CategoryList(ListView):
    model = Category
    

def show_by_category(request, category_name):
    try:
        category = Category.objects.get(slug=category_name)
        projects = Project.objects.filter(catergory=category)
        print(projects)
        return render(request,'campaign/showbyCategory.html',{'category':category, 'projects' : projects })
    except:
        return render(request, "notfound.html",{'msg':"category Not Found"}) 


def projects_list(request):
    try:
        projects=Project.AllProject()
        return render(request,"campaign/projects_list.html",{'projects':projects})
    except:
        return render(request, "notfound.html",{'msg':"projects Not Found"})

def project_detail(request, project_slug):
    try:
        project=Project.objects.get(slug=project_slug)
        all_reviews = Review.objects.filter(project=project)
        if request.method == 'POST':
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                review_form = review_form.save(commit=False)
                review_form.project = project
                review_form.user = request.user
                review_form.save()
                review_form = ReviewForm()

        else:
            review_form = ReviewForm()
        
        #handleing show project donations ---> ALIII
        donations_models = Donate.objects.filter(project=project)
        total_donations = 0
        for model in donations_models:
            total_donations += model.donation_amount
        return render(request,"campaign/projectdetail.html",{'project':project, 'review_form': review_form, 'all_reviews':all_reviews, 'total_donations': total_donations})
    
    except:
        return render(request, "notfound.html",{'msg':"project Not Found"})


@login_required
def delete_project(request,project_slug):
    try:
        project=Project.objects.get(slug=project_slug)
        if project.owner.id == User.id:
            if Donate.objects.filter(project=project).aggregate(Sum("donation_amount")) < project.target * 0.25:
                Project.delete_project(id)
                return redirect('showall')
            else:
                return render(request, "notfound.html",{'msg':"You Can't delete  this project!"})
        else:
            return render(request, "notfound.html",{'msg':"You Can't delete  this project!"})
    except:
        return render(request, "notfound.html",{'msg':"project Not Found"})


def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        projectimagesform = ProjectImagesForm(request.POST, request.FILES)
        if form.is_valid() and projectimagesform.is_valid():
            project =  form.save(commit=False)
            project.owner = request.user
            project.save()
            projectimagesform.save(project)
            # form.save_m2m()
    else:
        form = ProjectForm()
        projectimagesform = ProjectImagesForm()
    context = {
            'form':form,
            'projectimagesform' : projectimagesform 
        }
    return render(request, 'campaign/create_project.html', context)


def update_project(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    project_images = ProjectImage.objects.filter(project=project)
    print("here images",project_images)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form = form.save(commit=False)
            form.owner = request.user
            form.save()
        
            # for image in request.FILES.getlist('images'):
            #     project_image = ProjectImage.objects.create(project=form, image=image)
    else:
        form = ProjectForm(instance=project)
        # initial_images_data = [{'image': image.image} for image in project_images]
        # print("all images",initial_images_data)
        # # project_images_form = ProjectImagesForm(initial=initial_images_data)
        
    context = {'form': form}
    # context = {'form': form, 'project_images_form': project_images_form}
    return render(request, 'campaign/update_project.html', context)

def donate_project(request, project_slug):

    # try:
        project = get_object_or_404(Project, slug=project_slug)
        if request.method == 'POST':
            form = DonateForm(request.POST)
            if (form.is_valid()):
                form = form.save()
                print("Form saved")
                project_detail(request, project_slug=project_slug)
                return HttpResponseRedirect(reverse('project_details', kwargs= {'project_slug':project_slug}))
        form = DonateForm()
        context = {'form':form}
        return render(request,'campaign/donate_project.html', context=context )
    # except:
    #     return render(request, "notfound.html",{'msg':"project Not Found"})