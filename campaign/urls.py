from django.urls import path 
from .views import create_project, update_project

urlpatterns = [
    path('addproject/', create_project, name='add_project'),
    path('update/<slug:project_slug>', update_project, name='update_project'),

]
