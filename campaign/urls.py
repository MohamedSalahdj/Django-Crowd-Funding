from django.urls import path 
from .views import *

urlpatterns = [
    path("", projects_list, name='all_projects'),
    path("list-category", CategoryList.as_view(), name='category_list'),
    path("category/<slug:category_name>/", show_by_category, name="category"),
    path("project/<slug:project_slug>", project_detail, name="project_details"),
    path("deleteproject/<slug:project_slug>/", delete_project, name="deletproject"),
    path('addproject/', create_project, name='add_project'),
    path('update/<slug:project_slug>', update_project, name='update_project'),
]

