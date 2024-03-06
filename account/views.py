from django.shortcuts import render, reverse
from django.http import HttpResponse
# from django.http import HttpResponseRedirect
# from .models import *
# from .forms import *

# Create your views here.
def home(request):
  return render (request, 'base.html')

# def news_list(request):
#     return render(request, 'account/news.html')

# def news_detail(request):
#     return render(request, 'account/news-detail.html')

def donate(request):
    return render(request, 'account/donate.html')

def login(request):
    return render(request, 'account/login.html')

def register(request):
    return render(request, 'account/register.html')