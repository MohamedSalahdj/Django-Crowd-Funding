from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    phone = models.CharField(max_length=12,validators=[RegexValidator(regex="^01[0|1|2|5][0-9]{8}$",message="Phone must be start 010, 011, 012, 015 and all number contains 11 digits")],blank=True)
   
    image = models.ImageField(default="default.png",upload_to="account/images/",null=True ,blank=True)
    birth_date= models.DateField(null=True)
    facebook_profile= models.URLField(null=True,blank=True)
    country = models.CharField(max_length=20,blank=True,null=True)

    def __str__(self):
        return f"{self.user.username}"

