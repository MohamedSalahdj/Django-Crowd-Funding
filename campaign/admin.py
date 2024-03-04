from django.contrib import admin
from .models import Category, Project, ProjectImage

admin.site.register(Category)
admin.site.register(Project)
admin.site.register(ProjectImage)
