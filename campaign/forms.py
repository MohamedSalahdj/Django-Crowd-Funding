from django import forms
from .models import Project, ProjectImage, Review, Donate

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

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ('created_at', 'project', 'user')

class DonateForm(forms.ModelForm):
    """Rendring the donation as a form for the user"""

    class Meta:
        model = Donate
        exclude = ('donated_time',)