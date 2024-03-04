from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.template.defaultfilters import slugify



class Category(models.Model):
    name = models.CharField(max_length=20)

    def  __str__(self):
        return self.name
    
    @classmethod
    def AllCategory(cls):
        return cls.objects.all()
    
    @classmethod
    def  get_category(cls,id):
        return Category.objects.get(id=id)
    
    @classmethod
    def  delete_category(cls,id):
        return Category.objects.filter(id=id).delete()

    @classmethod
    def showCategory(cls):
        return [(i.id, i.name) for i in cls.objects.all()]



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
    def  delete_project(cls,id):
        return cls.objects.filter(id=id).delete()
    
    def GetImageURl(self):
        return f'/media/{self.image}'

class ProjectImage(models.Model):
    image = models.ImageField(upload_to='projects/images',blank=True,null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_images')
