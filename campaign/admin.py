from django.contrib import admin
from .models import Category, Project, ProjectImage, Review, Donate, ReplayComment

admin.site.register(Category)
admin.site.register(Project)
admin.site.register(ProjectImage)
admin.site.register(Donate)
admin.site.register(Review)
admin.site.register(ReplayComment)
