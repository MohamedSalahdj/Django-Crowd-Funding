from django import forms
from .models import Project, ProjectImage, Review, Donate, ReplayComment

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

class ReplayCommentForm(forms.ModelForm):
    class Meta:
        model = ReplayComment
        exclude = ('created_at', 'review_comment', 'user')

class DonateForm(forms.ModelForm):
    """Rendring the donation as a form for the user"""

    class Meta:
        model = Donate
        exclude = ('donated_time', 'donator', 'project')

    def __init__(self, *args, **kwargs):
        project = kwargs.pop('project', None)
        donator = kwargs.pop('donator', None)
        super(DonateForm, self).__init__(*args, **kwargs)
        self.project = project
        self.donator = donator

    def clean_donation_amount(self):
        donation_amount = self.cleaned_data.get('donation_amount')
        if donation_amount > self.project:
            raise forms.ValidationError("Donation amount cannot exceed the project target.")
        return donation_amount