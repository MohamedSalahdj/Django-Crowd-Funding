from django.urls import path 
from .views import *

urlpatterns = [
    path("", homepage, name='home_page'),
    path("projects/", projects_list, name='all_projects'),
    path("search/", homepage, name='search_project'),
    path("list-category/", CategoryList.as_view(), name='category_list'),
    path("category/<slug:category_name>/", show_by_category, name="category"),
    path("project/<slug:project_slug>", project_detail, name="project_details"),
    path("projects/deleteproject/<slug:project_slug>/", delete_project, name="deletproject"),
    path('projects/addproject/', create_project, name='add_project'),
    path('projects/update/<slug:project_slug>', update_project, name='update_project'),
    path('donate/<slug:project_slug>', donate_project, name='donate_project'),
    path('submit_reply/<int:review_id>/', submit_reply, name='submit_reply'),

]

