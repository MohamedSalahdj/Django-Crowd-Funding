from django.contrib import admin
from .models import *


#Register your models here.

# class userRegisterAdmin(admin.ModelAdmin):
#     list_display = ('user')


admin.site.register(Profile)