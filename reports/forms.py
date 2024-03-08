from django import forms
from .models import ReportProject, ReportReview

class ReportProjectForm(forms.ModelForm):
    class Meta:
        model = ReportProject
        exclude = ('created_at', 'project', 'reporter')
