from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils.text import slugify



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
    target=models.DecimalField(max_digits=10, decimal_places=2)
    start_date=models.DateField(auto_now_add=True)
    end_date=models.DateField()
    tags = TaggableManager()
    feature = models.BooleanField(default=False)
    slug = models.SlugField(null=True)

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

class ProjectImage(models.Model):
    image = models.ImageField(upload_to='projects/images',blank=True,null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_images')


    def __str__(self):
        return f'{self.project} -- {self.image.url}'