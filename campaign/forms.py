from django import forms
from .models import Project, ProjectImage

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ('owner', 'start_date', 'slug', 'feature')

class PrjectImagesForm(forms.ModelForm):
    class Meta:
        model = ProjectImage
        fields = '__all__'