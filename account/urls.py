from django.urls import path 
from .views import signup
from django.contrib.auth import views

urlpatterns = [
    path('signup/',signup,name='signup'),
    path('logout/',views.LogoutView.as_view,name='logout'),
    
    
    
]
