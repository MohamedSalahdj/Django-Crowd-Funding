from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from campaign.models import Project, Review

class ReportProject(models.Model):
    reason = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_report')
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_project_report')

    def __str__(self):
        return f'{self.reporter} - {self.project} - {self.reason}'

class ReportReview(models.Model):
    reason = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='review_report')
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_review_report')

    def __str__(self):
        return f"- {self.reporter} - '{self.reason}'"