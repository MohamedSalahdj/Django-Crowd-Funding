from django.urls import path 
from account.views import *

urlpatterns = [
    path('base/', home, name='home'),

    # path('news-list/', news_list, name='news_listing'),
    # path('news-detail/<int:news_id>/', news_detail, name='news_detail'),
    path('donate/', donate, name='donate'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
]
