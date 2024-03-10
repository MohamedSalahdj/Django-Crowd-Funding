from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils.text import slugify
from django.utils import timezone
from django.db.models.aggregates import Avg
from django import forms



class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(null=True, blank=True)
    def  __str__(self):
        return self.name
    
    @classmethod
    def AllCategory(cls):
        return cls.objects.all()
    
    @classmethod
    def  get_category(cls,id):
        return Category.objects.filter(id=id).first()
    
    @classmethod
    def  delete_category(cls,id):
        return Category.objects.filter(id=id).delete()

    @classmethod
    def showCategory(cls):
        return [(i.id, i.name) for i in cls.objects.all()]
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs) 


class Project(models.Model):
    title = models.CharField(max_length=20, unique=True)
    details = models.TextField()
    image = models.ImageField(upload_to='projects/images')
    catergory = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='projectCatergory')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projectUser')
    target = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    tags = TaggableManager()
    feature = models.BooleanField(default=False)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)

    def  __str__(self):
        return self.title

    @classmethod
    def AllProject(cls):
        return cls.objects.all()

    @classmethod
    def  get_project(cls,id):
        return cls.objects.get(id=id)
    
    @classmethod
    def  get_project_by_name(cls,title):
        return cls.objects.get(title=title)

    @classmethod
    def  delete_project(cls,id):
        return cls.objects.filter(id=id).delete()

    def GetImageURl(self):
        return self.image.url
    
    def similar_projects(self):
        similar_five_projects = Project.objects.filter(tags__in=self.tags.all()).exclude(id=self.id).distinct()
        return similar_five_projects[:5]  
    
    def avg_rate(self):
        avg = self.project_review.aggregate(project_avg=Avg('rate'))
        return round(avg['project_avg'], 2) if avg['project_avg'] else 0 

class ProjectImage(models.Model):
    image = models.ImageField(upload_to='projects/images',blank=True,null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_images')

    def __str__(self):
        return f'{self.project} -- {self.image.url}'
    

class Donate(models.Model):
    """ Donation relationship between the user and the project"""
    donation_amount = models.PositiveBigIntegerField()
    donated_time = models.DateTimeField(default=timezone.now)
    donator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project_donator')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='donated_project')

    def __str__(self):
        return f'{self.donation_amount} | {self.project} | {self.donator} | {self.donated_time}'
    
class Review(models.Model):
    comment = models.CharField(max_length=255)
    rate = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, related_name='user_review', on_delete=models.CASCADE)
    project = models.ForeignKey(Project, related_name='project_review', on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.user} | {self.project} | 'comment' --> {self.comment}"

class ReplayComment(models.Model):
    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, related_name='user_replay', on_delete=models.CASCADE)
    review_comment = models.ForeignKey(Review, on_delete=models.CASCADE,  related_name='replay_comment_review') 


    def __str__(self):
        return f'{self.comment}'