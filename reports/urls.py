from django.urls import path
from .views import report_comment


urlpatterns = [
    path('report-comment/<int:id>', report_comment, name='report_comment')
]
