from django.contrib import admin
from .models import Category, Project, ProjectImage,Donate
from .models import Category, Project, ProjectImage, Review

admin.site.register(Category)
admin.site.register(Project)
admin.site.register(ProjectImage)
admin.site.register(Donate)
admin.site.register(Review)
