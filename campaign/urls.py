from django.urls import path 
from .views import *

urlpatterns = [
    path("",show_all,name='all'),
    path("category/<int:id>/", show_by_category, name="category"),
    path("project/<slug:project_slug>", project_detail, name="detail"),
    path("deleteproject/<slug:project_slug>/", delete_project, name="deletproject"),
    path('addproject/', create_project, name='add_project'),
    path('update/<slug:project_slug>', update_project, name='update_project'),
]

