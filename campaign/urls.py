from django.urls import path 
from .views import *

urlpatterns = [
    path("",show_all,name='all'),
    path("category/<int:id>/", show_by_category, name="category"),
    path("project/<slug:title>", project_detail, name="detail"),
    path("deleteproject/<int:id>/", delete_project, name="deletproject"),

]
