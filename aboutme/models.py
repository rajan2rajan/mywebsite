from django.db import models
from tinymce.models import HTMLField
from datetime import date

# Create your models here.

class About(models.Model):
    detail = HTMLField()


class Videos(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False,unique=True)
    about_project = models.CharField(max_length=500,null=False,blank=False)
    video_link = models.URLField()
    date = models.DateField(default=date.today , blank=False,null=False)



# class detail(models.Model):
#     Name = 
#     address = 
#     phone_number = 
#     email = 
#     career_objective = 
#     maritial_stauts = 






