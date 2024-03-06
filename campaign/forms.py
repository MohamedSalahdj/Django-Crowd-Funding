from django import forms
from .models import Project, ProjectImage

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ('owner', 'start_date', 'slug', 'feature')

class ProjectImagesForm(forms.ModelForm):
    class Meta:
        model = ProjectImage
        exclude = ('project',)

    def save_images(self, project):
        for img in self.cleaned_data['images']:
            ProjectImage.objects.create(project=project, image=img)