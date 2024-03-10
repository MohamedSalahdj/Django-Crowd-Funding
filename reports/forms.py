from django import forms
from .models import ReportProject, ReportReview

class ReportProjectForm(forms.ModelForm):
    class Meta:
        model = ReportProject
        exclude = ('created_at', 'project', 'reporter')



class ReportCommentForm(forms.ModelForm):
    class Meta:
        model = ReportReview
        exclude = ('created_at', 'reporter', 'review')
