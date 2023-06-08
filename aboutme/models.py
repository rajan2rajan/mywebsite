from django.db import models
from tinymce.models import HTMLField
from datetime import date
from ckeditor.fields import RichTextField

# Create your models here.

class About(models.Model):
    detail = RichTextField(blank=False)


class Videos(models.Model):
    name = models.CharField(max_length=100,null=False,unique=True)
    about_project = models.CharField(max_length=500,null=False)
    thumbnail = models.ImageField(upload_to='image/',null=True,blank=True)
    
    video_link = models.CharField(max_length=500)
    date = models.DateField(default=date.today,null=False)



