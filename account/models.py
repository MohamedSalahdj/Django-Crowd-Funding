from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12,validators=[RegexValidator(regex="^01[0|1|2|5][0-9]{8}$",message="Phone must be start 010, 011, 012, 015 and all number contains 11 digits",code="invalid number")],blank=True)
   
    image = models.ImageField(default="default.jpg",upload_to="images/", blank=True)

    def __str__(self):
        return f"{self.user.username}"
